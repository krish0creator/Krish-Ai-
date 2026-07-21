import flet as ft
from ai import KrishAI

ai = KrishAI()


def main(page: ft.Page):
    page.title = "Krish AI"
    page.theme_mode = ft.ThemeMode.DARK
    page.window_width = 400
    page.window_height = 700
    page.padding = 15

    chat = ft.ListView(
        expand=True,
        spacing=10,
        auto_scroll=True,
    )

    user_input = ft.TextField(
        hint_text="Ask Krish AI...",
        expand=True,
        autofocus=True,
    )

    status = ft.Text("", color=ft.Colors.GREY)

    page.add(
        ft.Text(
            "🤖 Krish AI",
            size=28,
            weight=ft.FontWeight.BOLD,
        ),
        chat,
        status,
    )
    def send_message(e):
        text = user_input.value.strip()

        if not text:
            return

        chat.controls.append(
            ft.Text(f"🧑 You: {text}", selectable=True)
        )

        user_input.value = ""
        status.value = "⏳ Krish AI is thinking..."
        page.update()

        try:
            reply = ai.chat(text)

            chat.controls.append(
                ft.Text(f"🤖 Krish AI: {reply}", selectable=True)
            )

        except Exception as ex:
            chat.controls.append(
                ft.Text(f"❌ Error: {ex}", color=ft.Colors.RED)
            )

        status.value = ""
        page.update()

    send_btn = ft.ElevatedButton(
        "Send",
        on_click=send_message
    )

    page.add(
        ft.Row(
            [
                user_input,
                send_btn,
            ]
        )
    )


ft.run(main)
