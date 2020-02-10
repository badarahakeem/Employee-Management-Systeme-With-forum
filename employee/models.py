import datetime
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User

# from leave.models import Leave




# Create your models here.

class Role(models.Model):
    '''
       Table des rôles
    '''
    name = models.CharField(max_length=125)
    description = models.CharField(max_length=125,null=True,blank=True)

    created = models.DateTimeField(verbose_name=_('Created'),auto_now_add=True)
    updated = models.DateTimeField(verbose_name=_('Updated'),auto_now=True)


    class Meta:
        verbose_name = _('Role')
        verbose_name_plural = _('Roles')
        ordering = ['name','created']


    def __str__(self):
        return self.name




class Fliale(models.Model):
    '''
     Table des fliales
    '''
    name = models.CharField(max_length=125)
    description = models.TextField(max_length=250,null=True,blank=True)

    created = models.DateTimeField(verbose_name=_('Created'),auto_now_add=True)
    updated = models.DateTimeField(verbose_name=_('Updated'),auto_now=True)


    class Meta:
        verbose_name = _('Fliale')
        verbose_name_plural = _('Fliales')
        ordering = ['name','created']
    
    def __str__(self):
        return self.name




class Employee(models.Model):

    
    GENDER = (
    ('MALE','Male'),
    ('FEMALE','Female'),
    )


    TITLE = (
    ('MR','Mr'),
    ('MRS','Mrs'),
    ('MSS','Mss'),
    ('DR','Dr'),
    ('SIR','Sir'),
    ('MADAM','Madam'),
    )


    
    COMMUNES = (
    ('Dakar', 'Dakar'),('Guédiawaye','Guédiawaye'),('Pikine','Pikine'),('Bargny','Bargny'), ('Diamniadio','Diamniadio'), ('Rufisque','Rufisque'),
    ('Sébikhotane','Sébikhotane'), ('Bambey','Bambey'),('Diourbel','Diourbel'), ('Mbacké','Mbacké'), ('Diofior','Diofior'), ('Fatick','Fatick'),('Foundiougne','Foundiougne') ,
    ('Karang' ,'Karang') ,('Passy','Passy') ,('Sokone','Sokone'),('Soum','Soum'),('Gossas','Gossas'),('Birkelane','Birkelane'),('Kaffrine','Kaffrine'),('Nganda','Nganda'),
    ('Koungheul','Koungheul'),('Malem-Hodar','Malem-Hodar'),('Guinguinéo','Guinguinéo'),('Mboss','Mboss'),('Gandiaye','Gandiaye'),('Kahone','Kahone'),('Kaolack','Kaolack'),('Ndoffane','Ndoffane') ,
    ('Sibassor','Sibassor'),('Nioro_du_Rip','Nioro_du_Rip'),('keur_Madiabel','keur_Madiabel'),('Kédougou','Kédougou'),('Salemata','Salemata'),('Saraya','Saraya'), ('Kolda','Kolda'), ('Dabo','Dabo'), 
    ('Salikégné','Salikégné'),('Médina_Yoro_Foulah','Médina_Yoro_Foulah'), ('Pata','Pata'),('Vélingara','Vélingara'), ('Kounkané','Kounkané'), ('Diaobé_Kabendou','Diaobé_Kabendou'),
    ('Kébémer','Kébémer'), ('Guéoul','Guéoul'),('Dahra','Dahra'), ('Linguère','Linguère'),('Louga','Louga'), ('Ndiagne','Ndiagne'),('Niomré','Niomré'),('Dembakané','Dembakané'), ('Hamady_Hounaré','Hamady_Hounaré'), 
    ('Kanel','Kanel'), ('Semmé','Semmé'), ('Aouré','Aouré'),('Bokiladji','Bokiladji'), ('Sinthiou','Sinthiou'), ('Bamambé','Bamambé'),('Banadji','Banadji'), ('Waounde','Waounde'),('Matam','Matam'), ('Ourossogui','Ourossogui'), 
    ('Thilogne','Thilogne'), ('Agnam_Civol','Agnam_Civol'),('Bokidiawé','Bokidiawé'),('Ranérou','Ranérou'),('Dagana','Dagana'), ('Gaé','Gaé'),('Richard_Toll','Richard_Toll'),('Ross_Béthio','Ross_Béthio'), ('Rosso','Rosso'),('Aéré_Lao','Aéré_Lao') ,
    ('Bodé_Lao','Bodé_Lao'), ('Démette','Démette') ,('Galoya_Toucouleur','Galoya_Toucouleur'), ('Golléré','Golléré') ,('Guédé_Chantier','Guédé_Chantier'), ('Mboumba','Mboumba') , ('Niandane','Niandane'), ('Ndioum','Ndioum'), ('Pété','Pété') ,
    ('Podor','Podor') ,('Walaldé','Walaldé'), ('Saint_Louis','Saint_Louis'), ('Mpal','Mpal'),('Bounkiling','Bounkiling'),('Madina_Wandifa','Madina_Wandifa'),('Diattacounda','Diattacounda') , ('Goudomp','Goudomp'), ('Samine','Samine'), ('Tanaff','Tanaff'),
    ('Diannah_Malary','Diannah_Malary' ),('Marsassoum','Marsassoum'),('Sédhiou','Sédhiou'),('Bakel','Bakel'),('Diawara','Diawara') , ('Kidira','Kidira'),('Goudiry','Goudiry'), ('Kothiary','Kothiary'),('Koumpentoum','Koumpentoum'), ('Malem_Niani','Malem_Niani'),('Tambacounda','Tambacounda'),
    ('Joal_Fadiouth','Joal_Fadiouth'),  ('Mbour','Mbour'),('Ngaparou','Ngaparou') ,('Nguékhokh','Nguékhokh') ,('Popenguine_Ndayane','Popenguine_Ndayane'),('Saly_Portudal','Saly_Portudal'), ('Somone','Somone'),('Thiadiaye','Thiadiaye') ,('Ndiaganiao','Ndiaganiao'),
    ('Thiès','Thiès') ,('Kayar','Kayar') ,('Khombole','Khombole') ,('Pout','Pout'),('Mboro','Mboro') ,('Meckhe','Meckhe'), ('Tivaouane','Tivaouane'),('Bignona','Bignona'), ('Thionck_Essyl','Thionck_Essyl') , ('Diouloulou','Diouloulou'), ('Oussouye','Oussouye'),('Ziguinchor','Ziguinchor'),
    )



    # PERSONAL DATA
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name="employee" )
    title = models.CharField(_('Title'),max_length=10,default='MR',choices=TITLE,blank=False,null=True)
    image = models.FileField(_('Profile Image'),upload_to='profiles',default='default.png',blank=True,null=True,help_text='upload image size less than 2.0MB')#work on path username-date/image
    get_full_name = models.CharField(_('Fullname'),max_length=125,null=False,blank=False)
    sex = models.CharField(_('Gender'),max_length=8, default='MALE', choices=GENDER, blank=False)
    email = models.CharField(_('Email (optional)'),max_length=255,default=None,blank=True,null=True)
    tel = PhoneNumberField(default='+221771239025', null = False, blank=False, verbose_name='Phone Number (Example +221771239025)', help_text= 'Enter number with Country Code Eg. +221771239025')
    birthday = models.DateField(_('Birthday'),blank=False,null=False)
    place_of_birth = models.CharField(_('Region'),help_text='what town of the country(senegal) are you from ?', max_length=20, default='Dakar', choices=COMMUNES, blank=False, null=True)
    address = models.CharField(_('Address'),help_text='address of current residence',max_length=125,null=True,blank=True)


    # COMPANY DATA
    fliale =  models.ForeignKey(Fliale, verbose_name =_('Fliales'),on_delete=models.SET_NULL, null=True,default=None)
    role =  models.ForeignKey(Role,verbose_name =_('Role'),on_delete=models.SET_NULL,null=True,default=None)
    startdate = models.DateField(_('Employement Date'),help_text='date of employement',blank=False,null=True)

    #app related
    is_blocked = models.BooleanField(_('Is Blocked'),help_text='button to toggle employee block and unblock',default=False)
    is_deleted = models.BooleanField(_('Is Deleted'),help_text='button to toggle employee deleted and undelete',default=False)
 
    created = models.DateTimeField(verbose_name=_('Created'),auto_now_add=True,null=True)
    updated = models.DateTimeField(verbose_name=_('Updated'),auto_now=True,null=True)




   
    
    class Meta:
        verbose_name = _('Employee')
        verbose_name_plural = _('Employees')
        ordering = ['-created']



    def __str__(self):
        return self.get_full_name

    

    @property
    def get_age(self):
        current_year = datetime.date.today().year
        dateofbirth_year = self.birthday.year
        if dateofbirth_year:
            return current_year - dateofbirth_year
        return



   