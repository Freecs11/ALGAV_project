def moyenne_temps_construction(list_of_sizes):
#     list_of_times = []
#     for size in list_of_sizes:
#         list_of_times_for_size = []
#         for i in range(1,6):
#             list_of_values = st.treat_from_file("cles_alea/jeu_"+str(i)+"_nb_cles_"+str(size)+".txt")
#             start_time = time.time()
#             build_heap_table(list_of_values)
#             end_time = time.time()
#             list_of_times_for_size.append(end_time - start_time)
#         list_of_times.append(np.mean(list_of_times_for_size))
#     return list_of_times

# list_of_times = moyenne_temps_construction(list_of_sizes)
# plt.plot(list_of_sizes, list_of_times)
# plt.xlabel("taille de la lste")
# plt.ylabel("temps de construction")
# plt.title("temps de construction en fonction de la taille de la liste")
# plt.show()