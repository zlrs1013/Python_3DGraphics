"""
    test keyboard input. discrete, continuous and multiple inputs.
"""

from core.base import Base


# test input function
class Test(Base):

    def initialize(self):
        print("Initializing Program...")

    def update(self):

        #  debug printing
        if len(self.input.keyDownList) > 0:
            print(f"Keys down: {self.input.keyDownList}")

        elif len(self.input.keyUpList) > 0:
            print(f"Keys up: {self.input.keyUpList}")

        elif len(self.input.keyPressedList) > 0:
            print(f"Keys pressed: {self.input.keyPressedList}")

        # typical usage
        # if self.input.isKeyDown("space"):
        #     print("Hello")



# instantiate and run
Test().run()
