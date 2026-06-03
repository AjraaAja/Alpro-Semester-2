topi_list = [1, 2, 3, 4, 5] #angka yang tersembunyi di dalam topi pesulap
topi_list[2] = int(input("Masukkan angka untuk mengganti ke nilai tengah : "))
del topi_list[4]
print(len(topi_list))
print(topi_list)