#Você vai criar um sistema simples que simula o controle de um estacionamento. O sistema deve permitir registrar veículos, remover veículos e exibir os veículos que estão no estacionamento.
class Vehicle():
    def __init__(self, plate, type):
        self.plate = str(plate)
        self.type = str(type)
    def __str__(self):
        return f'\nPlaca: {self.plate}\nTipo: {self.type}'
class Parking():
    def __init__(self, total_vacancies):
        self.total_vacancies = total_vacancies
        self.occupie_vacancies = []
    def park_vehicle(self, vehicle):
        if len(self.occupie_vacancies) < self.total_vacancies:
            self.occupie_vacancies.append(vehicle)
            print('Estacionando..')
        else:
            print('Estacionamento cheio.')
    def remove_vehicle(self, plate):
        for vehicle in self.occupie_vacancies:
            if vehicle.plate == plate:
                self.occupie_vacancies.remove(vehicle)
                print(f'Veículo {vehicle} removido')
                return
        print(f'Veículo {plate} não encontrado.')
    def list_vehicles(self):
        if not self.occupie_vacancies:
            print('Nenhum veículo estacionado.')
        else:
            for vehicle in self.occupie_vacancies:
                print(vehicle)

vehicle_1 = Vehicle('FG84G', 'carro')
vehicle_2 = Vehicle('G84KJ', 'moto')
parking_1 = Parking(1)
parking_1.park_vehicle(vehicle_1)
parking_1.park_vehicle(vehicle_2)
parking_1.list_vehicles()