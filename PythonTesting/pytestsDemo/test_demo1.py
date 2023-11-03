#jakýkoli soubor pytest by měl začínat na test_ nebo končit na _test
#Název metody pytest by měl začínat na test
#Jakýkoli kód by měl být zabalen pouze do metody
#název metody by měl mít smysl
#-k znamená provedení názvů metod, -s odhlášení odhlášení - v znamená metada více informací
#můžete spustit konkrétní soubor pomocí py.test <název souboru>
#můžete označit tag testy @pytest.mark.smoke a běh pomocí -m
#můžete přeskočit testy s @pytest.mark.skip
import pytest
@pytest.fixture()
def setup():
    print("I will be executing first")
    yield
    print("I will executed last")

@pytest.mark.smoke
def test_firstProgram(setup):
   print("Hello")

@pytest.mark.xfail
def test_SecondGreetCreditCard():
    print("Good Morning")

