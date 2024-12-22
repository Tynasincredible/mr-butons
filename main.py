def on_button_pressed_a():
    basic.show_icon(IconNames.FABULOUS)
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_screen_up():
    basic.show_number(input.temperature())
input.on_gesture(Gesture.SCREEN_UP, on_gesture_screen_up)

def on_gesture_screen_down():
    music.play(music.builtin_playable_sound_effect(soundExpression.happy),
        music.PlaybackMode.IN_BACKGROUND)
input.on_gesture(Gesture.SCREEN_DOWN, on_gesture_screen_down)

def on_button_pressed_ab():
    music.play(music.tone_playable(311, music.beat(BeatFraction.WHOLE)),
        music.PlaybackMode.IN_BACKGROUND)
    basic.show_icon(IconNames.MEH)
    basic.clear_screen()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    music.play(music.tone_playable(311, music.beat(BeatFraction.WHOLE)),
        music.PlaybackMode.IN_BACKGROUND)
input.on_button_pressed(Button.B, on_button_pressed_b)
