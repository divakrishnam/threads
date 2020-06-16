# Threads
Threads in Python

### Lock
Lock merupakan tipe sinkronisasi simple pada python yang mempunyai dua state/keadaann yaitu locked dan unlocked. locked diimplementasikan di method acquire() dan unlocked diimplementasikan di method release()

### RLocks
RLocks digunakan ketika melakukan lock pada percabangan atau perulangan

### Semaphore
Semaphore menyediakan thread dengan sinkronisasi akses secara terbatas dari resource yang ada

### Event
Event merupakan tipe sinkronisasi yang mengantarkan pesan antar thread

### Condition
Condition digunakan tidak hanya menghantarkan pesan antar thread tapi memberitahukan perubahan state dari program

### Barrier
Barrier tipe sinkronisasi yang menggunakan berbagai thread yang berbeda yang saling menunggu satu sama lain selesai, dan menampilkan progress secara bersama-sama
