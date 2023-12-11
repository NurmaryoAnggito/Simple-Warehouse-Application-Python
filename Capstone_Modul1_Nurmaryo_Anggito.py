#membuat aplikasi gudang (stok) sederhana tanpa ui deadline 11 desember 2023
#class barang = IDBarang, Kategori, NamaBarang, Stok, Harga, Merek, Keterangan
from tabulate import tabulate
import sys
import random


#data default
KeyDictBarang = ['IDBarang','Kategori','NamaBarang','Stok','Harga','Merk']
ListBarang = [{
    'IDBarang' : '000001',
    'Kategori' : 'ALAT ELEKTRONIK',
    'NamaBarang' : 'BATERAI TIPE AAA MERK ABC',
    'Stok' : 100,
    'Harga' : 30000,
    'Merk' : 'ABC',
},{
    'IDBarang' : '000002',
    'Kategori' : 'ALAT ELEKTRONIK',
    'NamaBarang' : 'BOHLAM 20WATT MERK PHILLIPS',
    'Stok' : 30,
    'Harga' : 100000,
    'Merk' : 'PHILLIPS',
},{
    'IDBarang' : '000003',
    'Kategori' : 'ALAT RUMAH TANGGA',
    'NamaBarang' : 'VACUM CLEANER PHILLIPS',
    'Stok' : 40,
    'Harga' : 300000,
    'Merk' : 'PHILLIPS',
},{
    'IDBarang' : '000004',
    'Kategori' : 'ALAT DAPUR',
    'NamaBarang' : 'PANCI 5L',
    'Stok' : 25,
    'Harga' : 150000,
    'Merk' : 'COSMOS',
}]

#fungsi tampilkan menu utama
def ShowMainMenuFunction() :
    print('\n')
    print('Main Menu Gudang')
    print('1. Cek Stok Gudang.')
    print('2. Cari Data')
    print('3. Tambah Item ke Gudang.')
    print('4. Update Stok')
    print('5. Hapus Data Item')
    print('6. Keluar Program')
    Menu = str(input('Pilih Menu (1-6) : '))
    print('\n')
    return Menu                 #return kode untuk pilih menu

#fungsi tampilkan tabel data
def ShowdataFunction(data) :
    ListPrint = []
    for i in range(len(data)) :
        IdBarang = data[i]['IDBarang']
        KategoriBarang = data[i]['Kategori']
        NamaBarang = data[i]['NamaBarang']
        StokBarang = int(data[i]['Stok'])
        HargaBarang = int(data[i]['Harga'])
        MerkBarang = data[i]['Merk']
        ListPrint.append([IdBarang,KategoriBarang,NamaBarang,StokBarang,HargaBarang,MerkBarang])
    print('\n')
    print(tabulate(ListPrint,headers=KeyDictBarang))
    print('\n')


#fungsi kembali ke menu utama
def BacktoMainMenuFunction() :
    while True :
        Back = input('Kembali ke menu utama? (y/n) : ')
        if Back.upper() == 'Y' :
            break
        elif Back.upper() == 'N' :
            print('Anda keluar dari program.')
            sys.exit()                              #keluar dari program
        else :
            print('Inputan anda salah.')
            continue

#fungsi pilih kategori untuk update dan delete
#kategori berfungsi untuk membuat idbarang
def SelectItemCategoryFunction() :
    print('Pilih Kategori')
    print('1. ALAT RUMAH TANGGA')
    print('2. ALAT ELEKTRONIK')
    print('3. ALAT DAPUR')
    while True : 
        kodeKategori = input('Masukan angka kategori : ')
        match kodeKategori :
            case '1' : 
                kategori = 'ALAT RUMAH TANGGA'
                break
            case '2' :
                kategori = 'ALAT ELEKTRONIK'
                break
            case '3' :
                kategori = 'ALAT DAPUR'
                break
            case _ :
                print('Kategori tidak tersedia coba masukan kategori yang tersedia. ')
    return kategori

##generate uniqe id using random function dan kategori
def CreateUniqueIDFunction() :
    while True : 
        uniqueID = str(random.randint(100000,999999))
        if any(item['IDBarang'] == uniqueID for item in ListBarang) :
            uniqueID = str(random.randint(100000,999999))
        else : break
    return uniqueID

# fungsi tambah data baru dimulai dengan memilih kategori
# input nama, stok, harga, dan merk. uniqe id akan otomatis generate secara random
def AddNewItemFunction() :
    while True :
        NewItem = []
        KategoriBarang = SelectItemCategoryFunction() #pilih kategori
        IDBarang = CreateUniqueIDFunction()             #auto generate idbarang
        NewItem.append(IDBarang.upper())
        NewItem.append(KategoriBarang.upper())
        NamaBarang = input('Masukan Nama Barang : ')
        NewItem.append(NamaBarang.upper())
        while True :
            StokBarang = input('Masukan Jumlah Stok Barang : ')         #cek harus angka
            if StokBarang.isdigit() :
                NewItem.append(StokBarang)
                break
            else :
                print('Stok Barang harung angka, Mohon Masukan ulang')
                continue
        while True :
            HargaBarang = input('Masukan Harga Barang : ')              #cek harus angka
            if HargaBarang.isdigit() :
                NewItem.append(HargaBarang)
                break
            else :
                print('Harga Barang harung angka, Mohon Masukan ulang')
                continue
        MerkBarang = input('Masukan Merk Barang : ')
        NewItem.append(MerkBarang.upper())
        return NewItem

#fungsi select satu item dari tabel digunakan di menu update dan delete
def SelectItemFunction(cekmenu) : #parameter untuk memilih menu
    while True :
        if cekmenu == 'delete' :                    #untuk pilih menu yang dipakai
            IdBarang = input('Masukan ID Barang yang akan dihapus : ').upper()
        elif cekmenu == 'update' :
            IdBarang = input('Masukan ID Barang yang akan diupdate : ').upper()
        ItemSelected = []
        ID = any(item['IDBarang'] == IdBarang for item in ListBarang)       #cek value dari idbarang untuk setiap item dari list
        if ID :                                                             
            ItemSelected = [item for item in ListBarang if item.get('IDBarang') == IdBarang]
            break
        else :
            print('ID barang tidak ada, mohon masukan ID Barang yang sudah ada')
            continue
    return ItemSelected[0]  #return 1 item dictionary

#memilih kolom yang akan di update
def UpdateItemFunction(Kode,ItemUpdate) :
    while True :
        match Kode :
            case 1 :    #kategori
                kategori = SelectItemCategoryFunction()
                for item in ListBarang :
                    if item == ItemUpdate :
                        item['Kategori'] = kategori.upper()
                        return item
            case 2 :    #nama
                for item in ListBarang :        
                    if item == ItemUpdate :
                        value = input('Masukan nama pengganti : ')
                        item['NamaBarang'] = value.upper()
                        return item
            case 3 :    #stok
                for item in ListBarang :
                    while True :
                        value = input('Masukan stok pengganti : ')
                        if value.isdigit() : 
                            if item == ItemUpdate :
                                item['Stok'] = value
                                return item
                        else :
                            print('Harus angka')
                            continue
            case 4 :    #harga
                for item in ListBarang :        
                    while True :
                        value = input('Masukan harga pengganti : ')   
                        if value.isdigit() :     
                            if item == ItemUpdate :
                                item['Harga'] = value
                                return item
                        else :
                            print('Harus angka')
                            continue
            case 5 :    #merk
                for item in ListBarang :        
                    if item == ItemUpdate :
                        value = input('Masukan merk pengganti : ')
                        item['Merk'] = value.upper()
                        return item
            case _ :    #selain 1-5
                print('Menu tidak ada')
                continue    


#kembali ke menu sebelumnya
def ReturntoMenuFunction(Menu) :
    match Menu :
        case 'read' :
            while True :
                BackToAdd = input('Apakah ada data yang akan dicari lagi? (y/n) : ')    
                if BackToAdd.upper() == 'Y' :
                    break
                elif BackToAdd.upper() == 'N' :
                    BacktoMainMenuFunction()
                    break
                else :
                    print('Inputan anda salah.')
                    continue
        case 'add' :           
            while True :
                BackToAdd = input('Apakah ada data yang akan ditambah lagi? (y/n) : ')    
                if BackToAdd.upper() == 'Y' :
                    break
                elif BackToAdd.upper() == 'N' :
                    BacktoMainMenuFunction()
                    break
                else :
                    print('Inputan anda salah.')
                    continue
        case 'update' :
            while True :
                BackToAdd = input('Apakah ada data yang akan diupdate lagi? (y/n) : ')    
                if BackToAdd.upper() == 'Y' :
                    break
                elif BackToAdd.upper() == 'N' :
                    BacktoMainMenuFunction()
                    break
                else :
                    print('Inputan anda salah.')
                    continue
        case 'delete' :
            while True :
                BackToAdd = input('Apakah ada data yang akan dihapus lagi? (y/n) : ')    
                if BackToAdd.upper() == 'Y' :
                    break
                elif BackToAdd.upper() == 'N' :
                    BacktoMainMenuFunction()
                    break
                else :
                    print('Inputan anda salah.')
                    continue

#membuat list dari list utama ketika value ada di list utama
def SelectItemsbyValueFunction(list, value):
    selectedList = [item for item in list if any(value.upper() in str(x).upper() for x in item.values())]
    return selectedList
    

#code utama
while True :
    Menu = ShowMainMenuFunction()  #menu utama
    match Menu :

        # tampilkan data dummy/default
        case '1' :
            print('Daftar Stok Barang')
            ShowdataFunction(ListBarang)
            BacktoMainMenuFunction()

        #tampilkan data sesuai filter input
        case '2' :
            print('Menu Cari Data')
            filter = input('Masukan data yang akan dicari : ')
            selectedItem = SelectItemsbyValueFunction(ListBarang,filter.upper())
            if len(selectedItem) > 0 :
                ShowdataFunction(selectedItem)
            elif len(selectedItem) == 0 :
                print('Data tidak ada')
            ReturntoMenuFunction('read')
 
        #add new item
        case '3' :            
            ListNewItem = []        #list sementara
            print('Menu menambahkan barang baru')
            print('Daftar Stok Barang yang baru') #tampilkan data awal
            ShowdataFunction(ListBarang)
            NewItem = AddNewItemFunction()
            ListNewItem.append(NewItem)
            print('Barang yang akan ditambahkan')       #tampilkan data yang akan ditambahkan
            print(tabulate(ListNewItem,headers=KeyDictBarang))
            AddConfirmation = input('Menambahkan data barang baru sesuai data diatas? (y/n) : ')  #konfirmasi tambah data ke list utama
            if AddConfirmation.upper() == 'Y' :
                ListBarang.append(dict(zip(KeyDictBarang,NewItem)))         #casting list jadi dictionary dan ditambahkan ke list utama
                ShowdataFunction(ListBarang)
                ReturntoMenuFunction('add')
            elif AddConfirmation.upper() == 'N' :
                BacktoMainMenuFunction()
                break
            else :
                print('Inputan anda salah.')
                continue

        #update hanya bisa update stok barang
        case '4' :
            ListItemUpdate = []
            print('Menu update stok item ')
            ShowdataFunction(ListBarang)        #tampilkan data awal
            ItemUpdate = SelectItemFunction('update')     #pilih item yang akan diupdate sesuai input idbarang
            ListItemUpdate.append(list(ItemUpdate.values()))
            print('Barang yang akan diupdate') #tampilkan item yang akan di update
            print(tabulate(ListItemUpdate,headers=KeyDictBarang))
            print('Pilih Kolom')
            print('1. KATEGORI BARANG')
            print('2. NAMA BARANG')
            print('3. STOK BARANG')
            print('4. HARGA BARANG')
            print('5. MERK BARANG')
            MenuUpdate = int(input('Pilih Kolom yang akan diupdate : '))
            UpdatedItem = UpdateItemFunction(MenuUpdate,ItemUpdate)
            Confirmation = input('Apakah akan update data diatas? (y/n) : ') #konfirmasi update item
            if Confirmation.upper() == 'Y' :
                for item in ListBarang : 
                    if item.get('IDBarang') == ItemUpdate.get('IDBarang') :
                        item.update(UpdatedItem)                                 
                ShowdataFunction(ListBarang)
                ReturntoMenuFunction('update')
            elif Confirmation.upper() == 'N' :
                    BacktoMainMenuFunction()
                    break
            else :
                    print('Inputan anda salah.')
                    continue
            
        #delete item
        case '5' :
            ListItemDelete = []
            print('Menu menghapus barang di gudang')
            ShowdataFunction(ListBarang)        #tampilkan data awal
            ItemDelete = SelectItemFunction('delete')     #pilih item yang akan dihapus
            ListItemDelete.append(list(ItemDelete.values()))    
            print('Barang yang akan dihapus')           #tampilkan item yang akan dihapus
            print(tabulate(ListItemDelete,headers=KeyDictBarang))
            AddConfirmation = input('Apakah akang menghapus data diatas? (y/n) : ')
            if AddConfirmation.upper() == 'Y' :     #konfirmasi delete
                    ListBarang.remove(ItemDelete)
                    print('Daftar data yang telah dihapus')
                    ShowdataFunction(ListBarang)
                    ReturntoMenuFunction('delete')
            elif AddConfirmation.upper() == 'N' :
                    BacktoMainMenuFunction()
                    break
            else :
                    print('Inputan anda salah.')
                    continue
                
        #exit program
        case '6' :
            print('Terima kasih sudah menggunakan program ini')
            sys.exit()
        
        #other jika input menu selain 1-6 akan kembali ke menu utama
        case _ :
            print('Menu tidak ada')
            BacktoMainMenuFunction()
