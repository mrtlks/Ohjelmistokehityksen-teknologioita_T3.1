
import pytest
import postinumerot
import http_pyynto

toimipaikat = {

"16200" :"ARTJÄRVI",
"16201" : "ARTJÄRVI",
"49780" : "ONKAMAA",
"49400" : "HAMINA",
"49401" : "HAMINA",
"49420" : "HAMINA",
"49460" : "HAMINA",
"49461" : "HAMINA",
"16960" : "ISO-EVO",
"22550" : "VÅRDÖ",
"65374" : "SMART POST"
}

http_data = http_pyynto.hae_postinumerot() 


# aluksi "fixture 'hae_ryhmittely' not found" -virheilmoitus
# "Fixtures are defined using the @pytest.fixture decorator" https://docs.pytest.org/en/6.2.x/fixture.html
# "pytest fixtures are functions attached to the tests which run before the test function is executed"

@pytest.fixture 
def hae_ryhmittely():
     return postinumerot.ryhmittele_toimipaikoittain (toimipaikat)


@pytest.fixture 
def hae_http_datan_ryhmittely():
     return postinumerot.ryhmittele_toimipaikoittain(http_data)

#_______________________________________________________________________________

#TESTIT


#  1. verrataan avainta ja sen arvoa "toimipaikat" -datan arvoihin, kun arvoja on yksi
def test_vain_yksi_postinumero(hae_ryhmittely):

 assert hae_ryhmittely["ONKAMAA"] == ["49780"]


#  2.  verrataan avainta ja sen arvoa "toimipaikat" -datan arvoihin kun arvoja on kaksi + kyseessä erikoistapaus (ääkköset)
def test_kaksi_postinumeroa(hae_ryhmittely):

 assert hae_ryhmittely["ARTJÄRVI"] == ["16200", "16201"]


#  3.  verrataan listojen pituutta, kun arvoja on enemmän kuin kaksi
def test_enemmän_kuin_kaksi_postinumeroa():
 
 testi = postinumerot.listaa_postitoimipaikan_postinumerot("HAMINA", toimipaikat )

 assert len(testi) > 2


#_______________________________________________________________________________

# BUGI 

# Vertaamalla listojen pituuksia saadaan testi, jolla kaikkien kirjoitusasujen paikkansapitävyys selviää
# Kaikilla kirjoitusasuilla pitäisi tulla yhtä pitkä lista postinumeroita 



# Bugi korjattu ohjelmassa "postinumerot_bugi_korjattu"
def test_bugi_korjattu(): # tämä testi menee läpi

 smartpost = postinumerot.kasittele_bugi(http_data)
 smart_post = postinumerot.kasittele_bugi(http_data)
 smartpsot = postinumerot.kasittele_bugi(http_data)

 assert len(smartpost) == len(smart_post)==len(smartpsot)
 

 
