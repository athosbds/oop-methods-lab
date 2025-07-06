# Mostrar: 1) filmes que todos assistiram, 2) só 1 amigo assistiu, 3) 2 ou + assistiram, 4) não assistidos
lucas = {"Invocação do Mal", "Homem de Ferro", "Homem Aranha", "Matrix"}
maria = {"Homem de Ferro", "Zumbis", "Fim do Mundo", "Matrix"}
pedro = {"Invocação do Mal", "Fim do Mundo", "Outlet", "Matrix"}
todos_os_filmes = {"Invocação do Mal", "Como Treinar Seu Dragão","Homem de Ferro", "Homem Aranha", "Zumbis", "Fim do Mundo", "Outlet"}


set_watched = (lucas & maria) | (maria & pedro) | (pedro & lucas)
print(f'Filmes que 2 assistiram: {set_watched}')
set_movies = todos_os_filmes - (lucas | maria | pedro)
print(f'\nFilmes não assistidos por NINGUÉM: {set_movies}')
set_lucas = lucas - ( maria & pedro)
set_pedro = pedro - ( maria & lucas)
set_maria = maria - (pedro & lucas)
set_exclusive = set_lucas | set_pedro | set_maria
print(f'\nFilme que só 1 amigo assistiu: {set_exclusive}')
set_all = lucas & maria & pedro
print(f'\nFilmes Assistidos por Todos: {set_all}')