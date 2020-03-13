# -*- coding: utf-8 -*-
from drawille import Canvas, line, Turtle
from unittest import TestCase, main


class CanvasTestCase(TestCase):


    def test_set(self):
        canvas = Canvas()
        canvas.set(0, 0)
        self.assertTrue(0 in canvas.chars and 0 in canvas.chars[0])


    def test_unset_empty(self):
        canvas = Canvas()
        canvas.set(1, 1)
        canvas.unset(1, 1)
        self.assertEqual(len(canvas.chars), 0)


    def test_unset_nonempty(self):
        canvas = Canvas()
        canvas.set(0, 0)
        canvas.set(0, 1)
        canvas.unset(0, 1)
        self.assertEqual(canvas.chars[0][0], 1)


    def test_clear(self):
        canvas = Canvas()
        canvas.set(1, 1)
        canvas.clear()
        self.assertEqual(canvas.chars, dict())


    def test_toggle(self):
        canvas = Canvas()
        canvas.toggle(0, 0)
        self.assertEqual(canvas.chars, {0: {0: 1}})
        canvas.toggle(0, 0)
        self.assertEqual(canvas.chars, dict())


    def test_set_text(self):
        canvas = Canvas()
        canvas.set_text(0, 0, "asdf")
        self.assertEqual(canvas.frame(), "asdf")


    def test_frame(self):
        canvas = Canvas()
        self.assertEqual(canvas.frame(), '')
        canvas.set(0, 0)
        self.assertEqual(canvas.frame(), '⠁')


    def test_max_min_limits(self):
        canvas = Canvas()
        canvas.set(0, 0)
        self.assertEqual(canvas.frame(min_x=2), '')
        self.assertEqual(canvas.frame(max_x=0), '')


    def test_get(self):
        canvas = Canvas()
        self.assertEqual(canvas.get(0, 0), False)
        canvas.set(0, 0)
        self.assertEqual(canvas.get(0, 0), True)
        self.assertEqual(canvas.get(0, 1), False)
        self.assertEqual(canvas.get(1, 0), False)
        self.assertEqual(canvas.get(1, 1), False)


class LineTestCase(TestCase):


    def test_single_pixel(self):
        self.assertEqual(list(line(0, 0, 0, 0)), [(0, 0)])


    def test_row(self):
        self.assertEqual(list(line(0, 0, 1, 0)), [(0, 0), (1, 0)])


    def test_column(self):
        self.assertEqual(list(line(0, 0, 0, 1)), [(0, 0), (0, 1)])


    def test_diagonal(self):
        self.assertEqual(list(line(0, 0, 1, 1)), [(0, 0), (1, 1)])


class TurtleTestCase(TestCase):


    def test_position(self):
        turtle = Turtle()
        self.assertEqual(turtle.pos_x, 0)
        self.assertEqual(turtle.pos_y, 0)
        turtle.move(1, 1)
        self.assertEqual(turtle.pos_x, 1)
        self.assertEqual(turtle.pos_y, 1)


    def test_rotation(self):
        turtle = Turtle()
        self.assertEqual(turtle.rotation, 0)
        turtle.right(30)
        self.assertEqual(turtle.rotation, 30)
        turtle.left(30)
        self.assertEqual(turtle.rotation, 0)


    def test_brush(self):
        turtle = Turtle()
        self.assertFalse(turtle.get(turtle.pos_x, turtle.pos_y))
        turtle.forward(1)
        self.assertTrue(turtle.get(0, 0))
        self.assertTrue(turtle.get(turtle.pos_x, turtle.pos_y))
        turtle.up()
        turtle.move(2, 0)
        self.assertFalse(turtle.get(turtle.pos_x, turtle.pos_y))
        turtle.down()
        turtle.move(3, 0)
        self.assertTrue(turtle.get(turtle.pos_x, turtle.pos_y))


if __name__ == '__main__':
    main()
