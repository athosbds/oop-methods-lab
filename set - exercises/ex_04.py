# Mostrar: 1) filmes que todos assistiram, 2) só 1 amigo assistiu, 3) 2 ou + assistiram, 4) não assistidos
lucas = {"Invocação do Mal", "Homem de Ferro", "Homem Aranha"}
maria = {"Homem de Ferro", "Zumbis", "Fim do Mundo"}
pedro = {"Invocação do Mal", "Fim do Mundo", "Outlet"}
todos_os_filmes = {"Invocação Do Mal", "Homem de Ferro", "Homem Aranha", "Zumbis", "Fim do Mundo", "Outlet"}


set_watched = (lucas & maria) | (maria & pedro) | (pedro & lucas)
set_exclusive = pedro - (lucas | maria)