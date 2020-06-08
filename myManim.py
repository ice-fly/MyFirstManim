from manimlib.imports import *

class MyFirstManim(Scene):
	CONFIG = { "plane_3" : { 
		"x_line_frequency" :3,
		"y_line_frequency" :3
		}, 
	"point_charge_loc" : 0.5*RIGHT-1.5*UP,
	}
	def construct(self):
		name_text = TextMobject(
			"Alexander M Lanyi"
		)
		name_text.set_color(TEAL)

		self.play(Write(name_text),run_time=6)


		description_text = TextMobject(
			"High-Quality Math Animations"
		)
		description_text.set_color(LIGHT_GREY)
		description_text.scale(0.5)
		description_text.shift(2.4*DOWN)

		my_plane = NumberPlane(**self.plane_3)
		my_plane.add(my_plane.get_axis_labels())

		self.add(description_text)
		self.play(ApplyMethod(name_text.shift,2*DOWN),FadeIn(my_plane),run_time=4)

		field = VGroup(*[self.calc_field(x*RIGHT+y*UP)
			for x in np.arange(-9,9,1)
			for y in np.arange(-5,5,1)
			])

		self.wait(0.8)
		self.play(FadeOut(name_text),FadeOut(description_text),run_time=3)

		draw_field = VGroup(*field)  
		draw_field.set_color(PURPLE)

		self.play(ShowCreation(draw_field),run_time=2.8)
		self.play(ApplyMethod(draw_field.rotate,(TAU/8)),run_time=1.2)
		self.play(ApplyMethod(draw_field.scale,1.3),run_time=1)
		self.play(ApplyMethod(draw_field.shift,.2*DOWN),run_time=1)
		self.wait(2)
		self.play(ApplyMethod(draw_field.shift,.2*UP),run_time=1)
		self.play(ApplyMethod(draw_field.scale,1/1.3),run_time=1)
		self.play(ApplyMethod(draw_field.rotate,TAU-(TAU/8)),run_time=1.2)
		self.play(FadeOut(draw_field),FadeOut(my_plane),run_time=2.8)
		self.wait(1)

	def calc_field(self,point):
		x,y = point[:2]
		Rx,Ry = self.point_charge_loc[:2]
		r = (x+math.sqrt((x-Rx)**2 + (y-Ry)**2))/3
		efield = np.array(( -2*(y%3)+1 , -2*(x%2)+1 , 0 ))/3
		return Vector(efield).shift(point)