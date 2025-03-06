import customtkinter as ctk
from tkinter import filedialog
import schedule
import time
import threading

# Configurar o tema
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class InterfaceApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Agendador de Backups")
        self.geometry("700x500")

        # Criando um frame para os campos de origem e destino
        self.frame_paths = ctk.CTkFrame(self)
        self.frame_paths.pack(pady=10, padx=20, fill="x")

        # Campo para selecionar pasta de origem
        self.label_origem = ctk.CTkLabel(self.frame_paths, text="Pasta de Origem:", width=180)
        self.label_origem.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.entry_origem = ctk.CTkEntry(self.frame_paths, width=300)
        self.entry_origem.grid(row=0, column=1, padx=10, pady=5, sticky="w")
        self.btn_origem = ctk.CTkButton(self.frame_paths, text="Selecionar", command=self.selecionar_origem, width=100)
        self.btn_origem.grid(row=0, column=2, padx=10, pady=5)

        # Campo para selecionar pasta de destino
        self.label_destino = ctk.CTkLabel(self.frame_paths, text="Pasta de Destino:", width=180)
        self.label_destino.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.entry_destino = ctk.CTkEntry(self.frame_paths, width=300)
        self.entry_destino.grid(row=1, column=1, padx=10, pady=5, sticky="w")
        self.btn_destino = ctk.CTkButton(self.frame_paths, text="Selecionar", command=self.selecionar_destino, width=100)
        self.btn_destino.grid(row=1, column=2, padx=10, pady=5)

        # Título do agendador
        self.texto_descricao = ctk.CTkLabel(self, text="Opções Agendador", font=("Arial", 15))
        self.texto_descricao.pack(pady=10)

        # Criando um frame para os campos de agendamento
        self.frame_horario_frequencia = ctk.CTkFrame(self)
        self.frame_horario_frequencia.pack(pady=10, padx=20, fill="x")

        # Campo de horário
        self.label_horario = ctk.CTkLabel(self.frame_horario_frequencia, text="Horário (HH:MM):", width=180)
        self.label_horario.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.entry_horario = ctk.CTkEntry(self.frame_horario_frequencia, width=150, placeholder_text="Formato 24h")
        self.entry_horario.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        # Campo de frequência
        self.label_frequencia = ctk.CTkLabel(self.frame_horario_frequencia, text="Frequência:", width=180)
        self.label_frequencia.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.frequencia = ctk.CTkComboBox(self.frame_horario_frequencia, values=["Diariamente", "Semanalmente", "Mensalmente"], width=150, command=self.atualizar_opcoes)
        self.frequencia.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        # Frame para opções extras (dias da semana ou dia do mês)
        self.frame_opcoes_extras = ctk.CTkFrame(self)
        self.frame_opcoes_extras.pack(pady=10, padx=20, fill="x")

        # Checkboxes para selecionar dias da semana (com espaçamento reduzido)
        self.dias_semana = ["Seg", "Ter", "Qua", "Qui", "Sex", "Sáb", "Dom"]
        self.check_vars = {dia: ctk.BooleanVar() for dia in self.dias_semana}
        self.checkboxes = []
        for i, dia in enumerate(self.dias_semana):
            cb = ctk.CTkCheckBox(self.frame_opcoes_extras, text=dia, variable=self.check_vars[dia])
            cb.grid(row=0, column=i, padx=5, pady=5, sticky="w")  # Reduzi o padx e pady para ajustar melhor
            self.checkboxes.append(cb)

        # Configuração para garantir que as colunas sejam menores e mais compactas
        for i in range(7):  # Como são 7 dias, ajustamos o tamanho das colunas
            self.frame_opcoes_extras.grid_columnconfigure(i, weight=1, minsize=40)

        # Campo para selecionar o dia do mês
        self.label_dia_mes = ctk.CTkLabel(self.frame_opcoes_extras, text="Dia do Mês:")
        self.entry_dia_mes = ctk.CTkEntry(self.frame_opcoes_extras, width=50, placeholder_text="1-31")
        self.label_dia_mes.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.entry_dia_mes.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        # Ocultar campos extras no início
        self.frame_opcoes_extras.pack_forget()

        # Botão para iniciar o agendamento
        self.btn_iniciar = ctk.CTkButton(self, text="Iniciar Agendamento", command=self.iniciar_agendamento)
        self.btn_iniciar.pack(pady=20)

    def selecionar_origem(self):
        pasta_origem = filedialog.askdirectory()
        if pasta_origem:
            self.entry_origem.delete(0, ctk.END)
            self.entry_origem.insert(0, pasta_origem)

    def selecionar_destino(self):
        pasta_destino = filedialog.askdirectory()
        if pasta_destino:
            self.entry_destino.delete(0, ctk.END)
            self.entry_destino.insert(0, pasta_destino)

    def atualizar_opcoes(self, escolha):
        """ Atualiza os campos extras dependendo da frequência escolhida. """
        self.frame_opcoes_extras.pack_forget()
        for cb in self.checkboxes:
            cb.grid_remove()
        self.label_dia_mes.grid_remove()
        self.entry_dia_mes.grid_remove()

        if escolha == "Semanalmente":
            self.frame_opcoes_extras.pack(pady=5, padx=10, fill="x")
            for cb in self.checkboxes:
                cb.grid()
        elif escolha == "Mensalmente":
            self.frame_opcoes_extras.pack(pady=5, padx=10, fill="x")
            self.label_dia_mes.grid(row=1, column=0, padx=10, pady=5, sticky="w")
            self.entry_dia_mes.grid(row=1, column=1, padx=10, pady=5, sticky="w")
        elif escolha == "Diariamente":
            # Não há opções extras para o agendamento diário
            self.frame_opcoes_extras.pack_forget()

    def iniciar_agendamento(self):
        origem = self.entry_origem.get()
        destino = self.entry_destino.get()
        horario = self.entry_horario.get()
        freq = self.frequencia.get()

        if not origem or not destino or not horario:
            print("Preencha todos os campos!")
            return

        def tarefa_backup():
            print(f"Realizando backup de {origem} para {destino}...")

        # Configurar agendamento com o Schedule
        if freq == "Diariamente":
            schedule.every().day.at(horario).do(tarefa_backup)
        elif freq == "Semanalmente":
            dias_selecionados = [dia for dia, var in self.check_vars.items() if var.get()]
            for dia in dias_selecionados:
                if dia == "Seg":
                    schedule.every().monday.at(horario).do(tarefa_backup)
                elif dia == "Ter":
                    schedule.every().tuesday.at(horario).do(tarefa_backup)
                elif dia == "Qua":
                    schedule.every().wednesday.at(horario).do(tarefa_backup)
                elif dia == "Qui":
                    schedule.every().thursday.at(horario).do(tarefa_backup)
                elif dia == "Sex":
                    schedule.every().friday.at(horario).do(tarefa_backup)
                elif dia == "Sáb":
                    schedule.every().saturday.at(horario).do(tarefa_backup)
                elif dia == "Dom":
                    schedule.every().sunday.at(horario).do(tarefa_backup)
        elif freq == "Mensalmente":
            dia_mes = self.entry_dia_mes.get()
            print(f"Backup agendado para o dia {dia_mes} de cada mês às {horario}")
            schedule.every().month.at(f"{horario}:00").do(tarefa_backup)

        # Criar thread para rodar o agendamento
        threading.Thread(target=self.executar_agendamento, daemon=True).start()

    def executar_agendamento(self):
        while True:
            schedule.run_pending()
            time.sleep(1)

# Executar a aplicação
app = InterfaceApp()
app.mainloop()
