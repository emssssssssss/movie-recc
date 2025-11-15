import gradio as gr
import pandas as pd

# Supponi di avere già una funzione che, dato il profilo utente e feedback (like/dislike), restituisce la lista finale
def consigli_personalizzati(personality_dict, already_seen):
    # Qui metti il tuo codice che genera la lista finale come DataFrame!
    # Ad esempio:
    film_finale = ... # richiede le logiche già provate
    return film_finale[['title', 'genres', 'predicted_rating']]

# Componenti Gradio
personality_inputs = [
    gr.Slider(1, 5, step=0.1, label="Estroversione (E)"),
    gr.Slider(1, 5, step=0.1, label="Amicalità (A)"),
    gr.Slider(1, 5, step=0.1, label="Coscienziosità (C)"),
    gr.Slider(1, 5, step=0.1, label="Stabilità Emotiva (S)"),
    gr.Slider(1, 5, step=0.1, label="Apertura Mentale (O)")
]

with gr.Blocks() as demo:
    gr.Markdown("# Raccomandatore di Film personalizzato")
    gr.Markdown(
        "Inserisci il tuo profilo oppure compila il quiz, poi clicca per scoprire i film consigliati!"
    )
    input_personality = gr.Group(personality_inputs)
    seen_input = gr.Textbox(label="MovieId dei film già visti (separati da virgola)", placeholder="Es: 101,202,303")

    btn = gr.Button("Scopri i suggerimenti")
    output_table = gr.Dataframe(
        headers=["Title", "Genres", "Predicted Rating"],
        label="Film consigliati"
    )

    def raccomanda(E, A, C, S, O, already_seen):
        profilo_utente = {'E': E, 'A': A, 'C': C, 'S': S, 'O': O}
        # parsing degli id già visti
        already_seen_list = [int(x.strip()) for x in already_seen.split(',') if x.strip().isdigit()]
        # logica su tuoi dati
        final_table = consigli_personalizzati(profilo_utente, already_seen_list)
        return final_table

    btn.click(
        raccomanda,
        inputs=[personality_inputs[0], personality_inputs[1], personality_inputs[2],
                personality_inputs[3], personality_inputs[4], seen_input],
        outputs=output_table
    )

demo.launch()
