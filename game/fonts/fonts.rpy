init python:
    # Roboto font - Excelente suporte para português com cedilha e acentos
    config.font_replacement_map["Roboto.ttf", False, False] = ("fonts/Roboto-Regular.ttf", False, False)
    config.font_replacement_map["Roboto.ttf", True, False] = ("fonts/Roboto-Bold.ttf", False, False)
    config.font_replacement_map["Roboto.ttf", True, True] = ("fonts/Roboto-BoldItalic.ttf", False, False)
    config.font_replacement_map["Roboto.ttf", False, True] = ("fonts/Roboto-Italic.ttf", False, False)
    # Default font which supports CJK.
    config.font_replacement_map["SourceHanSans.ttf", False, False] = ("fonts/SourceHanSans-Light.ttc", False, False)
    config.font_replacement_map["SourceHanSans.ttf", True, False] = ("fonts/SourceHanSans-Bold.ttc", False, False)

    # Coder font.  Trigged by {tt} tag.
    def coder_font(tag, argument, contents):

        return [ (renpy.TEXT_TAG, u"font=fonts/Inconsolata-Regular.ttf") ] + contents + [ (renpy.TEXT_TAG, u"/font") ]

    config.custom_text_tags["tt"] = coder_font
    config.custom_text_tags["code"] = coder_font

style default:
    font FontGroup().add("Roboto.ttf", 0x0020, 0x024f).add("SourceHanSans.ttf", 0x0000, 0xffff)
