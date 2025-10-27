import tkinter as tk
from datetime import datetime
import webbrowser
from news import load_news  # deve retornar lista de tuplas (titulo, url)


def tela_noticias():
    def abrir_link(url):
        """Abre o link da notícia no navegador padrão"""
        webbrowser.open_new_tab(url)

    def on_enter(event):
        """Quando o mouse entra no texto"""
        event.widget.config(fg="#0052cc", font=("Helvetica", 12, "underline"))

    def on_leave(event):
        """Quando o mouse sai do texto"""
        event.widget.config(fg="black", font=("Helvetica", 12))

    def atualizar_noticias():
        # Limpa o conteúdo anterior
        for widget in frame_lista_noticias.winfo_children():
            widget.destroy()

        # Carrega as notícias (lista de tuplas: título, link)
        todas_noticias = load_news()
        noticias_atuais = todas_noticias[:4]  # mostra apenas as 4 primeiras

        hora_atual = datetime.now().strftime("%H:%M:%S")

        # Cria um label clicável para cada notícia
        for i, (titulo, link) in enumerate(noticias_atuais, start=1):
            lbl = tk.Label(
                frame_lista_noticias,
                text=f"{i}. {titulo}",
                font=("Helvetica", 12),
                fg="black",
                bg="white",
                anchor="w",
                justify="left",
                cursor="hand2",
                wraplength=420
            )
            lbl.pack(fill="x", pady=6)

            # Eventos de interação
            lbl.bind("<Enter>", on_enter)
            lbl.bind("<Leave>", on_leave)
            lbl.bind("<Button-1>", lambda e, url=link: abrir_link(url))

        lbl_atualizacao.config(text=f"Última atualização: {hora_atual}")

    # Janela principal
    janela = tk.Tk()
    janela.title("Últimas Notícias")
    janela.configure(bg="#e6f2ff")
    janela.resizable(False, False)

    screen_width = janela.winfo_screenwidth()
    screen_height = janela.winfo_screenheight()
    window_width = int(screen_width * 0.4)
    window_height = int(screen_height * 0.5)
    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2
    janela.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    # Topo
    top_frame = tk.Frame(janela, bg="#0052cc", height=int(window_height * 0.15))
    top_frame.pack(fill="x")

    titulo = tk.Label(
        top_frame,
        text="📰 Últimas Notícias",
        font=("Helvetica", 20, "bold"),
        fg="white",
        bg="#0052cc"
    )
    titulo.place(relx=0.5, rely=0.5, anchor="center")

    # Área de conteúdo
    frame_conteudo = tk.Frame(janela, bg="#ffffff", padx=20, pady=20)
    frame_conteudo.pack(fill="both", expand=True, pady=10)

    frame_lista_noticias = tk.Frame(frame_conteudo, bg="white")
    frame_lista_noticias.pack(fill="both", expand=True)

    # Botão Atualizar
    frame_botoes = tk.Frame(frame_conteudo, bg="white")
    frame_botoes.pack(pady=15)

    btn_atualizar = tk.Button(
        frame_botoes,
        text="Atualizar Notícias",
        bg="#0052cc",
        fg="white",
        font=("Helvetica", 12, "bold"),
        width=18,
        command=atualizar_noticias
    )
    btn_atualizar.pack()

    # Label de hora de atualização
    lbl_atualizacao = tk.Label(
        janela,
        text="Última atualização: --:--:--",
        bg="#e6f2ff",
        font=("Helvetica", 9)
    )
    lbl_atualizacao.pack(side="bottom", pady=5)

    # Rodapé
    rodape = tk.Label(
        janela,
        text="© 2025 Felipe da Silva | Portfólio",
        bg="#e6f2ff",
        font=("Helvetica", 9)
    )
    rodape.pack(side="bottom", pady=5)

    # Primeira carga de notícias
    atualizar_noticias()

    janela.mainloop()


if __name__ == '__main__':
    tela_noticias()
