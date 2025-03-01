class SplineHistory:

    def __init__(self) -> None:
        self.spline_history = []
        self.spline_index = -1

    def add_cur_spline(self, self_knots):
        self.spline_history.append(self_knots[-1])

    def get_cur_spline(self):
        return self.spline_history
    
    def increase_spline_index(self):
        self.spline_index += 1

    def decrease_spline_index(self):
        self.spline_index -= 1  #for Undo action

    def get_last_spline_index(self):
        # print(f'{self.last_spline_index} - spline {self.get_cur_spline()}  - all spline history: {self.spline_history}')
        return self.spline_index
    
    # def get_previous_spline(self):
    #     index = self.decrease_last_spline_index()
    #     print(f'cur spline: {self.get_cur_spline()},   previous spline: {self.spline_history}')
    #     return self.spline_history[index]