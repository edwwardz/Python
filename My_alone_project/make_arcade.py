import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "EXAMPLE")

arcade.start_render()

x = 300
y = 300
radius = 200
arcade.draw_circle_filled(x, y, radius, arcade.color.YELLOW)

x = 370
y = 350
radius = 20
arcade.draw_circle_filled(x, y, radius, arcade.color.BLACK)

x = 230
y = 350
radius = 20
arcade.draw_circle_filled(x, y, radius, arcade.color.BLACK)

x = 300
y = 280
widht = 120
height = 100
start_angle = 190
end_angle = 350
arcade.draw_arc_outline(x, y, widht, height, arcade.color.BLACK, start_angle, end_angle, 10)

arcade.finish_render()

arcade.run()
