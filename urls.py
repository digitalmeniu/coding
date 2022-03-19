from django.urls import path
from . import views


urlpatterns = [

    path('login/', views.loginPage, name='login'),
    path('logout/',views.logoutUser,name ='logout'),

    path('', views.home,name="home"),
    path('user/',views.userPage,name='user-page'),





    path('pacient/<str:pk_test>/', views.pacient, name="pacient"),
    path('fisa_pacient/<str:pk_test>/', views.fisa_pacient, name="fisa_pacient"),
    path('lista_pacienti/', views.lista_pacienti, name="lista_pacienti"),
    path('lista_pacienti_doc/', views.lista_pacienti_doc, name="lista_pacienti_doc"),
    path('createPacientnou/', views.createPacientnou, name="createPacientnou"),

    path('updatePacient/<str:pk>/', views.updatePacient, name='updatePacient'),
    path('deletePacient/<str:pk>/', views.deletePacient, name='deletePacient'),


    path('lista_doctori/', views.lista_doctori, name="lista_doctori"),
    path('doctor/<str:pk_test>/', views.doctor, name="doctor"),
    path('doctor1', views.doctor1, name="doctor1"),
    path('program_doctor/', views.program_doctor, name="program_doctor"),
    path('program_doctor_id/<str:pk>/', views.program_doctor_id, name="program_doctor_id"),
    path('createDoctornou/', views.createDoctornou, name="createDoctornou"),
    path('deleteDoctor/<str:pk>/', views.deleteDoctor, name='deleteDoctor'),
    path('account/', views.accountSettings, name="account"),

    path('lista_programari/', views.lista_programari, name="lista_programari"),
    path('createProgramarenou/', views.createProgramarenou, name="createProgramarenou"),
    path('updateProgramare/<str:pk>/', views.updateProgramare, name='updateProgramare'),
    path('updateProgramareFisaNoua/<str:pk>/', views.updateProgramareFisaNoua, name='updateProgramareFisaNoua'),
    path('updateProgramareNoua/<str:pk>/', views.updateProgramareNoua, name='updateProgramareNoua'),
    path('deleteProgramare/<str:pk>/', views.deleteProgramare, name='deleteProgramare'),

    path('cabinetul_implantologie/', views.cabinetul_implantologie, name="cabinetul_implantologie"),
    path('cabinetul_endodontie/', views.cabinetul_endodontie, name="cabinetul_endodontie"),
    path('rapoarte/', views.rapoarte, name="rapoarte"),
    path('show/', views.show, name="show"),
    path('grafic_anual_total/', views.grafic_anual_total, name="grafic_anual_total"),
    path('grafic_anual_doctori/', views.grafic_anual_doctori, name="grafic_anual_doctori"),


    path('fisa_pdf/<str:pk>/', views.fisa_pdf, name ="fisa_pdf"),
    #path('save1', views.save1, name="save1"),





]



