input.onButtonPressed(Button.A, function () {
    counterA += 1
    basic.showIcon(IconNames.Fabulous)
    basic.clearScreen()
})
input.onGesture(Gesture.ScreenUp, function () {
    screen_up += 10
    counterA += screen_up
})
input.onGesture(Gesture.ScreenDown, function () {
    music.play(music.builtinPlayableSoundEffect(soundExpression.happy), music.PlaybackMode.InBackground)
})
input.onButtonPressed(Button.AB, function () {
    music.play(music.tonePlayable(311, music.beat(BeatFraction.Whole)), music.PlaybackMode.InBackground)
    basic.showIcon(IconNames.Meh)
    basic.clearScreen()
})
input.onButtonPressed(Button.B, function () {
    basic.showNumber(counterA)
    music.play(music.tonePlayable(311, music.beat(BeatFraction.Whole)), music.PlaybackMode.InBackground)
})
input.onPinPressed(TouchPin.P1, function () {
    counterA = 0
})
let screen_up = 0
let counterA = 0
counterA = 0
screen_up = 0
