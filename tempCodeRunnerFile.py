
# def moyenne_temps_union_table(list_of_sizes):
#     list_of_times = []
#     for size in list_of_sizes:
#         list_of_times_for_size = []
#         for i in range(1,5 , 2):
#             list_of_values1 = st.treat_from_file("cles_alea/jeu_"+str(i)+"_nb_cles_"+str(size)+".txt")
#             list_of_values2 = st.treat_from_file("cles_alea/jeu_"+str(i+1)+"_nb_cles_"+str(size)+".txt")
#             heap1 = build_heap_tree(list_of_values1)
#             heap2 = build_heap_tree(list_of_values2)
#             start_time = time.time()
#             Union2(heap1, heap2)
#             end_time = time.time()
#             list_of_times_for_size.append(end_time - start_time)
#         list_of_times.append(np.mean(list_of_times_for_size))
#     return list_of_times

# list_of_times = moyenne_temps_union_table(list_of_sizes)
# plt.clf()
# plt.plot(list_of_sizes, list_of_times)
# plt.xlabel("taille de la lste")
# plt.ylabel("temps d'union")
# plt.title("temps d'union en fonction de la taille de la liste")
# # plt.show()
# plt.savefig("experiments/temps_d_union_tree.png")
