class Actor:

    def __init__(self, actor_full_name: str):
        if actor_full_name == "" or type(actor_full_name) is not str:
            self.__actor_full_name = None
        else:
            self.__actor_full_name = actor_full_name.strip()

        self.colleague_list = []

    @property
    def actor_full_name(self) -> str:
        return self.__actor_full_name

    def add_actor_colleague(self, colleague):
        self.colleague_list.append(colleague.__actor_full_name)

    def check_if_this_actor_worked_with(self, colleague):
        if colleague.__actor_full_name in self.colleague_list:
            return True
        else:
            return False

    def __repr__(self):
        return f"<Actor {self.__actor_full_name}>"

    def __eq__(self, other):
        return not self < other and not other < self
        pass

    def __lt__(self, other):
        return self.__actor_full_name < other.__actor_full_name
        pass

    def __hash__(self):
        return hash(self.__actor_full_name)
        pass
