from manim import *

class BasicTriangle(Scene):
    def construct(self):
        triangle = Triangle()
        triangle.set_fill(BLUE, opacity=0.5)
        self.play(Create(triangle))

class ThreeTriangles(Scene):
    def construct(self):
        outer = Triangle()
        inners = [Triangle().scale(0.5).align_to(outer, dir)
                  for dir in [[0, 0.5, 1], [-1, -.5, 0], [1, -.5, 0]]]
        self.play(Create(outer))
        self.wait(0.5)
        inners[0].set_fill(RED, opacity=0.5)
        inners[1].set_fill(GREEN, opacity=0.5)
        inners[2].set_fill(BLUE, opacity=0.5)
        self.play([Create(triangle) for triangle in inners])

class InnerTriangle(Scene):
    def construct(self):
        outer = Triangle()
        inner = Triangle().rotate(PI).scale(0.5).align_to(outer, DOWN)
        self.play(Create(outer), Create(inner))

class NestOneTriangle(Scene):
    def construct(self):
        outer = Triangle()
        inners = [Triangle().scale(0.5).align_to(outer, dir)
            for dir in [[0, 0.5, 1], [-1, -.5, 0], [1, -.5, 0]]]
        top_inners = [Triangle().scale(0.25).align_to(inners[0], dir)
            for dir in [[0, 0.5, 1], [-1, -.5, 0], [1, -.5, 0]]]
        self.play(
            Create(outer),
            [Create(inner) for inner in inners],
            [Create(inner) for inner in top_inners]
        )

class NestOneGeneration(Scene):
    def construct(self):
        base = Triangle()
        inners = self.get_inners(base, 1)
        self.play(
            Create(base),
            [Create(t) for t in inners]
        )

    def get_inners(self, outer, gen):
        inners = [Triangle().scale(0.5**gen).align_to(outer, dir)
                for dir in [[0, 0.5, 1], [-1, -.5, 0], [1, -.5, 0]]]
        for inner, color in zip(inners, [RED, GREEN, BLUE]):
            inner.set_fill(color, opacity=0.5)
        return inners
    
class Sierpinski(Scene):
    def construct(self):
        base = Triangle()
        inners = self.nest_inners(base, 1, 3)
        #generations = [flatten_list(ts) for ts in inners]
        #for gen in generations:
        #    self.play([Create(t) for t in gen])
        #    self.pause(0.5)
        self.play(
            Create(base),
            [Create(t) for t in flatten_list(inners)]
        )

    def nest_inners(self, outer, gen, max_gen):
        inners = [Triangle().scale(0.5**gen).move_to(outer, dir)
                for dir in [[0, 1, 0], [-1, -1, 0], [1, -1, 0]]]
        for inner, color in zip(inners, [RED, GREEN, BLUE]):
            inner.set_fill(color, opacity=0.5)
        if gen == max_gen:
            return inners
        else:
            return [self.nest_inners(inner, gen+1, max_gen) for inner in inners]
        
def flatten_list(nested_list):
    flattened = []
    for item in nested_list:
        if isinstance(item, list):
            flattened.extend(flatten_list(item))
        else:
            flattened.append(item)
    return flattened