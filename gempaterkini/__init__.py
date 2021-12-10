import requests
from bs4 import BeautifulSoup

class GempaTerkini:
    def __init__(self):
        self.description = 'to get the latest eartquake news from BMKG'
        self.result = None

    def extraksi_data(self):
        """

            Tanggal: 06 Desember 2021
            Waktu: 21:24:11 WIB
            magnitudo: 4.5
            Kedalaman: 15 km
            Lokasi :7.74 LS - 119.03 BT
            Keterangan: Pusat gempa berada di laut 85 km TimurLaut Bima
            Dirasakan: Dirasakan (Skala MMI): III Bima
            :return:
        """
        try:
            content = requests.get('https://www.bmkg.go.id/')
        except Exception:
            return None
        if content.status_code == 200:
            soup = BeautifulSoup(content.text, 'html.parser')
            result = soup.find('span', {'class': 'waktu'})
            result = result.text.split(',')
            tanggal = result[0]
            waktu = result[1]

            result = soup.find('div', {'class': 'col-md-6 col-xs-6 gempabumi-detail no-padding'})
            result = result.findChildren('li')

            i=0
            magnitudo =None
            kedalaman =None
            ls = None
            bt = None
            lokasi = None
            dirasakan =None


            for data in result:
                if i == 1:
                    magnitudo = data.text
                elif i == 2:
                    kedalaman = data.text
                elif i == 3:
                    koordinat = data.text.split (' - ')
                    ls = koordinat[0]
                    bt = koordinat[1]
                elif i == 4:
                    lokasi = data.text
                elif i == 5:
                    dirasakan = data.text
                i = i + 1

            hasil = dict()
            hasil['tanggal'] = tanggal #"06 Desember 2021"
            hasil['waktu'] = waktu #"21:24:11 WIB"
            hasil['magnitudo'] = magnitudo
            hasil['kedalaman'] = kedalaman
            hasil['koordinat'] = {"ls": ls, "bt": bt}
            hasil['lokasi'] = lokasi
            hasil['dirasakan'] = dirasakan

            self.result = hasil
        else:
            return None


    def tampilkan_data(self):
        if self.result is None:
            print("Data tidak bisa ditampilkan")
            return

        print(f"Tanggal {self.result['tanggal']}")
        print(f"Waktu {self.result['waktu']}")
        print(f"Magnitudo {self.result['magnitudo']}")
        print(f"Kedalaman {self.result['kedalaman']}")
        print(f"Koordinat: LS={self.result['koordinat']['ls']}, BT={self.result['koordinat']['bt']}")
        print(f"Dirasakan{self.result['dirasakan']}")
        print(f"Lokasi{self.result['lokasi']}")

    def run(self):
        self.extraksi_data()
        self.tampilkan_data()

if __name__ == '__main__':
    gempa_di_indonesia = GempaTerkini()
    print('deskripsi package', gempa_di_indonesia.description)
    gempa_di_indonesia.run()
    # gempa_di_indonesia.extraksi_data()
    # gempa_di_indonesia.tampilkan_data()
