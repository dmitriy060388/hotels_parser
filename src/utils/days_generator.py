import datetime


class DaysGenerator:

    def one_day_generate(self):

        self.current_date = datetime.date.today()
        self.delta_date = datetime.timedelta(days=1)
        self.time = (
            datetime.datetime.now(datetime.timezone.utc) + self.delta_date
        )
        self.next_date = self.time.strftime("%Y-%m-%d")

    def get_date(self):
        self.current_date = datetime.date.today()
        self.delta_date = datetime.timedelta(days=1)
        self.time = (
            datetime.datetime.now(datetime.timezone.utc) + self.delta_date
        )
        self.next_date = self.time.strftime("%Y-%m-%d")

        return str(self.current_date) + ' ' + str(self.next_date)

    def week_generate(self):

        count = 0
        self.days_list = []
        while count < 7:
            self.current_date = datetime.date.today()
            self.next_date = self.current_date + datetime.timedelta(days=1)
            self.end = str(self.current_date) + ' ' + str(self.next_date)
            count += 1
            self.days_list.append(str(self.current_date))
            self.days_list.append(str(self.next_date))
            while count < 7:
                self.current_date = self.next_date
                self.next_date = self.current_date + datetime.timedelta(days=1)
                self.end = str(self.current_date) + ' ' + str(self.next_date)
                count += 1
                self.days_list.append(str(self.current_date))
                self.days_list.append(str(self.next_date))
        return self.days_list
