
# def moyenne_temps_ajout(list_of_values):
#     list_of_times_heaptable = []
#     list_of_times_binomialQueue = []
#     list_of_times_heaptree = []
#     heaptable = MinHeapTable()
#     binomialQueue = BinomialQueue()
#     heaptree = MinHeapBinaryTree()
#     for i in list_of_values:
#         start_time = time.perf_counter()
#         heaptable.ajout(i)
#         end_time = time.perf_counter()
#         list_of_times_heaptable.append(end_time - start_time)
#         start_time = time.perf_counter()
#         hp = BinomialHeap()
#         hp.ajout(i)
#         binomialQueue.ajout(hp)
#         end_time = time.perf_counter()
#         list_of_times_binomialQueue.append(end_time - start_time)
#         start_time = time.perf_counter()
#         heaptree.ajout(i)
#         end_time = time.perf_counter()
#         list_of_times_heaptree.append(end_time - start_time)
#     return list_of_times_heaptable, list_of_times_binomialQueue, list_of_times_heaptree

# heaptable_times, binomialQueue_times, heaptree_times = moyenne_temps_ajout(list_tree)

# # Create a list of the average times
# avg_times = [np.mean(heaptable_times), np.mean(binomialQueue_times), np.mean(heaptree_times)]

# # Create a list of the names of the data structures
# data_structures = ['heaptable', 'binomialQueue', 'heaptree']
# plt.clf()
# # Create a bar chart
# plt.bar(data_structures, avg_times)

# plt.xlabel('Data Structure')
# plt.ylabel('Average Ajout Time (seconds)')
# plt.title("Average Ajout Time for Different Data Structures")

# plt.savefig("experiments/etude_exp/temps_de_ajout.png")
