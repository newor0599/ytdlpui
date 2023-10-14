import flet as ft,os,time, easygui

def main(page: ft.Page) -> None:
    #Page setting
    page.title = "youtube downloader"
    """page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'"""
    page.window_height = 400
    page.window_width = 700
    page.window_left = -10
    page.window_top = 0
    page.window_resizable = True
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER


    #functions
    def change_dir(e):
        destination_input.value = easygui.diropenbox(title="Select a folder")
        page.update()

    def convert_vid(e):
        #Download configuration
        link = link_input.value
        downloadToPath = destination_input.value
        ytdlpPath = r"%USERPROFILE%"

        #Download command
        convert_cmd = rf'{ytdlpPath}\yt-dlp.exe -o "{downloadToPath}\%(title)s.%(ext)s" --no-mtime --default-search "ytsearch" {link}'

        #Download start's here
        if link != "":
            info_label.value = "Downloading..."
            page.update()
            os.system(convert_cmd)
            info_label.value = "Download complete"
            page.update()
            time.sleep(1)
            info_label.value = ""
            page.update()
        else:
            info_label.value = "Link cannot be empty"
            page.update()
            time.sleep(1)
            info_label.value = ""
            page.update()


    #Main
    link_input = ft.TextField(label="YouTube link",width=400,height=30,border_radius=20,text_size=13,content_padding=ft.Padding(10,0,10,0))
    destination_input = ft.TextField(value=r"%USERPROFILE%\Downloads",label="Destination",width=400,height=30,border_radius=20,text_size=13,content_padding=ft.Padding(10,0,10,0))
    destination_btn = ft.ElevatedButton("Change destination")
    convert_button = ft.ElevatedButton(text="Convert",width=200)
    info_label = ft.Text(value="")
    #element function
    convert_button.on_click = convert_vid
    destination_btn.on_click = change_dir
    #Rendering
    page.add(link_input,destination_input,destination_btn,convert_button,info_label)
    page.update()

if __name__ == "__main__":
    ft.app(target=main)