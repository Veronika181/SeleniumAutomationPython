#jakýkoli soubor pytest by měl začínat na test_ nebo končit na _test
#Název metody pytest by měl začínat na test
#Jakýkoli kód by měl být zabalen pouze do metody
#název metody by měl mít smysl
#-k znamená provedení názvů metod, -s odhlášení odhlášení - v znamená metada více informací
#můžete spustit konkrétní soubor pomocí py.test <název souboru>
#můžete označit tag testy @pytest.mark.smoke a běh pomocí -m
#můžete přeskočit testy s @pytest.mark.skip
#příslušenství se používají jako metody nastavení a odstranění pro soubor test case-conftest ke zobecnění
#příslušenství a zpřístupnit je všem testovacím případům
#datadriven a parametrizaci lze provést pomocí příkazů return ve formátu n-tice
#když definujete rozsah zařízení pro třídu, spustí se pouze jednou před zahájením třídy a na konci

# Any pytest file should start with test_ or end with _test
#pytest method names should start with test
#Any code should be wrapped in method only
import pytest



@pytest.mark.smoke
def test_firstProgram(setup):
    print("Hello")


@pytest.mark.xfail
def test_SecondGreetCreditCard():
    print("Good Morning")


def test_crossBrowser(crossBrowser):
    print(crossBrowser[1])
