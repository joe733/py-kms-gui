"""
App GUI definition
"""

# standard
from inspect import cleandoc
from tkinter import LEFT

# external
import customtkinter as ctk


__all__ = ['generate_frame']

# Modes: 'System' (standard), 'Dark', 'Light'
ctk.set_appearance_mode('System')
# Themes: 'blue' (standard), 'green', 'dark-blue'
ctk.set_default_color_theme('blue')


def __frame_layout(this: ctk.CTk):
    """Frame Layout"""
    # configure grid layout (1x2)
    this.grid_rowconfigure(0, weight=1)
    this.grid_columnconfigure(1, weight=1)

    this.frame_left = ctk.CTkFrame(
        master=this,
        width=180,
        corner_radius=0
    )
    this.frame_left.grid(row=0, column=0, sticky='nswe')

    this.frame_right = ctk.CTkFrame(master=this)
    this.frame_right.grid(row=0, column=1, sticky='nswe')


def __left_frame(this: ctk.CTk):
    """Left Frame"""
    # configure grid layout (7x1)
    # empty row with minsize as spacing
    this.frame_left.grid_rowconfigure(0, minsize=10)
    # empty row as spacing
    this.frame_left.grid_rowconfigure(6, weight=1)
    # empty row with minsize as spacing
    this.frame_left.grid_rowconfigure(8, minsize=20)
    # empty row with minsize as spacing
    this.frame_left.grid_rowconfigure(11, minsize=10)

    this.label = ctk.CTkLabel(
        master=this.frame_left,
        text='KMS Manager',
        text_font=('Roboto', -16)  # font name and size in px
    )
    this.label.grid(row=1, column=0, pady=10, padx=10)

    this.install_button = ctk.CTkButton(
        master=this.frame_left,
        text='Start',
        command=this.start_kms
    )
    this.install_button.grid(row=2, column=0, pady=10, padx=20)

    this.remove_button = ctk.CTkButton(
        master=this.frame_left,
        text='Stop',
        command=this.stop_kms
    )
    this.remove_button.grid(row=3, column=0, pady=10, padx=20)

    this.service_status = ctk.CTkLabel(
        master=this.frame_left,
        text='',
        text_font=('Roboto', -10)  # font name and size in px
    )
    this.service_status.grid(row=4, column=0, pady=10, padx=10)

    this.label_mode = ctk.CTkLabel(
        master=this.frame_left, text='Appearance:'
    )
    this.label_mode.grid(row=9, column=0, pady=0, padx=20, sticky='w')

    this.mode_option = ctk.CTkOptionMenu(
        master=this.frame_left,
        values=['Light', 'Dark', 'System'],
        command=this.change_appearance_mode
    )
    this.mode_option.grid(row=10, column=0, pady=10, padx=20, sticky='w')


def __right_frame(this: ctk.CTk):
    """Right Frame"""
    # configure grid layout (3x7)
    this.frame_right.rowconfigure((0, 1, 2, 3), weight=1)
    this.frame_right.rowconfigure(7, weight=10)
    this.frame_right.columnconfigure((0, 1), weight=1)
    this.frame_right.columnconfigure(2, weight=0)

    this.info_frame = ctk.CTkFrame(master=this.frame_right)
    this.info_frame.grid(
        row=0, column=0, rowspan=10, columnspan=4,
        padx=20, pady=10, sticky='nsew'
    )

    this.frame_bottom = ctk.CTkFrame(master=this.frame_right, fg_color=None)
    this.frame_bottom.grid(
        row=10, column=0, rowspan=1, columnspan=2,
        padx=20, pady=20, sticky='nsew'
    )

    this.instructions = ctk.CTkLabel(
        master=this.info_frame,
        text=cleandoc(
            """
                # Steps for Windows activation
                1. Start the server & open command prompt as administrator
                2. To install activation key, type:
                \tslmgr /ipk <YOUR_LICENSE_KEY>
                3. To configure server, type:
                \tslmgr /ipk localhost:1688
                Then to activate, type:
                \tslmgr /ato\n
                # Steps for Office activation
                1. Start the server & open command prompt as administrator and goto office directory:
                \tcd /d %ProgramFiles%\Microsoft Office\Office16
                2. To convert to volume license, type:
                \tfor /f %x in ('dir /b ..\\root\Licenses16\ProPlus2021VL_KMS*.xrm-ms')\r\tdo cscript ospp.vbs /inslic:"..\\root\Licenses16\%x"
                3. To activate, type:
                \tcscript ospp.vbs /setprt:1688
                \tcscript ospp.vbs /unpkey:<LAST_4_CHARACTERS_OF_YOUR_KEY> >nul
                \tcscript ospp.vbs /inpkey:<YOUR_LICENSE_KEY>
                \tcscript ospp.vbs /sethst:localhost
                \tcscript ospp.vbs /act
            """
        ),
        justify=LEFT,
    )
    this.instructions.grid(
        row=0, column=0, padx=20, pady=20, sticky='nswe'
    )

    this.project_info = ctk.CTkLabel(
        master=this.frame_bottom,
        text='Created by Jovial Joe Jayarson',
        # width=120,
        # corner_radius=6,  # <- custom corner radius
        # fg_color=('white', 'gray38'),  # <- custom tuple-color
        justify=LEFT
    )
    this.project_info.grid(
        row=0, column=0, columnspan=2,
        padx=0, pady=0, sticky='nwe',
    )

    this.button_5 = ctk.CTkButton(
        master=this.frame_right,
        text='Quit',
        border_width=2,
        fg_color=None,
        hover_color='#B71C1C',
        command=this.on_closing,
    )
    this.button_5.grid(
        row=10, column=2, columnspan=1,
        padx=20, pady=0, sticky='we'
    )


def __frame_defaults(this: ctk.CTk):
    """Default behavior"""
    # set default values
    this.mode_option.set('System')


def generate_frame(this: ctk.CTk):
    """Generate Frame"""
    width = 780
    height = 520

    this.geometry(f'{width}x{height}')
    this.minsize(width=width, height=height)
    # this.maxsize(width=width, height=height)

    # call .on_closing() when app gets closed
    this.protocol('WM_DELETE_WINDOW', this.on_closing)

    __frame_layout(this)  # create two frames
    __left_frame(this)  # left frame
    __right_frame(this)  # right frame
    __frame_defaults(this)  # set frame defaults
