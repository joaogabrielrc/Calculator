# @author: João Gabriel Cardoso
# @github: github.com/joaogabrielrc


class Calculation():

    def exe_calculation(self, input_value):
        self.input_value = self.set_calc(input_value)
        result = "0"

        try:
            result = eval(self.input_value)
            result = str(result)
            if len(result) > 8:
                result = '{:5.2E}'.format(float(result))

        except:
            result = "Erro"

        return result

    def set_calc(self, input_value):
        value = input_value
        
        if "x" in value:
            value = value.replace("x", "*")

        return value