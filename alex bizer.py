import numpy as np

class Node:
    """
        Sebuah node untuk A* Search
        parent adalah parent dari Node awal
        position adalah posisi awal Node didalam Maze (labirin)
        g adalah biaya untuk memulai pada Node awal
        h adalah dasar heuristik untuk menentukan biaya dari Node awal hingga Node tujuan akhir
        f adalah total biaya pada Node yang sedang dituju, f = g + h
    """

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0
    def __eq__(self, other):
        return self.position == other.position

# Fungsi berikut ini mendapatkan nilai path pencarian
def return_path(current_node,maze):
    path = []
    no_rows, no_columns = np.shape(maze)
    # here we create the initialized result maze with -1 in every position
    # 
    result = [[-1 for i in range(no_columns)] for j in range(no_rows)]
    current = current_node
    while current is not None:
        path.append(current.position)
        current = current.parent
    # Kembalikan path yang terbalik arah karena kita perlu memperlihatkan path dari awal ke akhir
    path = path[::-1]
    start_value = 0
    # lakukan update path yang telah ditemukan dengan increment (peningkatan) bertambah 1
    for i in range(len(path)):
        result[path[i][0]][path[i][1]] = start_value
        start_value += 1
    return result


def search(maze, cost, start, end):
    """
        Returns a list of tuples as a path from the given start to the given end in the given maze
        :param maze:
        :param cost
        :param start:
        :param end:
        :return:
    """

    # buat node awal dan akhir dengan inisialisasi nilai g, h dan f
    start_node = Node(None, tuple(start))
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, tuple(end))
    end_node.g = end_node.h = end_node.f = 0

    # Inisialisasi yet_to_visit dan visited_list
    # dalam list ini seluruh node yang berada pada yet_to_visit akan dilihat
    # dari sini kita akan memenuhi node dengan nilai terendah untuk pergerakan berikutnya
    yet_to_visit_list = []  
    # visited_list akan menyimpan semua node yang telah dipreiksa
    visited_list = [] 
    
    #Tambahkan node awal
    yet_to_visit_list.append(start_node)
    
    # Tambahkan kondisi untuk berhenti untuk menghindari loop tanpa batas
    # eksekusi dilakukan setelah beberapa langkah (yang telah ditentukan)
    outer_iterations = 0
    max_iterations = (len(maze) // 2) ** 10

    # Kotak mana yang kita cari, pergerakannya adalah kiri-kanan-atas-bawah
    # berupa 4 pergerakan untuk setiap posisi.

    move  =  [[-1, 0 ], # bergerak ke atas
              [ 0, -1], # bergerak ke kiri
              [ 1, 0 ], # bergerak ke bawah
              [ 0, 1 ]] # bergerk ke kanan

    # lihat jumlah baris dan kolom dari maze
    no_rows, no_columns = np.shape(maze)
    
    # Lakukan loop hingga ditemukan bagian akhir
    
    while len(yet_to_visit_list) > 0:
        
        # Setiap kali terdapat node yang berada daftar yet_to_visit maka nilai counter akan bertambah
        outer_iterations += 1    
        
        # Ambil node baru
        current_node = yet_to_visit_list[0]
        current_index = 0
        for index, item in enumerate(yet_to_visit_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index
                
        # Jika nilai untuk path terdapat dalam kondisi dibawah, 
        # maka kemungkinan tidak ada solusi atau nilai komputasi terlalu tinggi
        if outer_iterations > max_iterations:
            print ("kesulitan menemukan path karena terlalu banyak iterasi")
            return return_path(current_node,maze)

        # pop keluar node yang berada pada list yet_to_visit, tambahkan pada list yang telah diperiksa
        yet_to_visit_list.pop(current_index)
        visited_list.append(current_node)

        # Periksa apakah node tujuan telah dicapai, jika ya maka path telah ditemukan.
        if current_node == end_node:
            return return_path(current_node,maze)

        # Buat node children pada semua posisi yang bersebelahan dengan posisi kotak saat ini
        children = []

        for new_position in move: 

            # Lihat posisi node
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Pastikan node berada dalam area maze
            if (node_position[0] > (no_rows - 1) or 
                node_position[0] < 0 or 
                node_position[1] > (no_columns -1) or 
                node_position[1] < 0):
                continue

            # Pastikan node bisa bergerak
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            # Buat node baru
            new_node = Node(current_node, node_position)

            # Tambahkan node baru
            children.append(new_node)

        # Loop melalui children node
        for child in children:
            
            # Periksa semua visited_list untuk mengetahui semua child yang berada pada list 
            if len([visited_child for visited_child in visited_list if visited_child == child]) > 0:
                continue

            # Tentukan nilai f,g dan h
            child.g = current_node.g + cost
            # Nilai heuritik dihitung berdasarkan eucledian distance
            child.h = (((child.position[0] - end_node.position[0]) ** 2) + 
                       ((child.position[1] - end_node.position[1]) ** 2)) 

            child.f = child.g + child.h

            # Periksa apakah Child ada pada list yet_to_visit dan nilai g telah lebih rendah dari nilai sebelumnya.
            if len([i for i in yet_to_visit_list if child == i and child.g > i.g]) > 0:
                continue

            # Tambahkan child ke list yet_to_visit
            yet_to_visit_list.append(child)
if __name__ == '__main__':

    maze = [[0, 1, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 0],
            [0, 1, 0, 1, 0, 0],
            [0, 1, 0, 1, 1, 0],
            [0, 0, 0, 0, 1, 0]]
    
    start = [0, 0] # posisi awal
    end = [4,5] # posisi akhir
    cost = 2 # biaya pergerakan

    path = search(maze,cost, start, end)
    print(path)

print('\n'.join([''.join(["{:" ">3d}".format(item) for item in row]) 
      for row in path]))
