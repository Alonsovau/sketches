# 子类中扩展property
class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._name = value

    @name.deleter
    def name(self):
        raise AttributeError("Can't delete attribute")


class SubPerson(Person):
    @property
    def name(self):
        print('Getting name')
        return super().name

    @name.setter
    def name(self, value):
        print('Setting name to', value)
        super(SubPerson, SubPerson).name.__set__(self, value)

    @name.deleter
    def name(self):
        print('Deleting name')
        super(SubPerson, SubPerson).name.__delete__(self)


s = SubPerson('IU')
print(s.name)


class SubPerson2(Person):
    @Person.name.getter
    def name(self):
        print('Getting name2')
        return super().name


s2 = SubPerson2('suzy')
print(s2.name)


# A descriptor 描述器
class String:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        instance.__dict__[self.name] = value


# A class with descriptor
class PersonWithDesc:
    name = String('name')

    def __init__(self, name):
        self.name = name


class SubPersonWithDesc(PersonWithDesc):
    @property
    def name(self):
        print('Getting name')
        return super().name

    @name.setter
    def name(self, value):
        print('Setting name to', value)
        super(SubPersonWithDesc, SubPersonWithDesc).name.__set__(self, value)

    @name.deleter
    def name(self):
        print('Deleting name')
        super(SubPersonWithDesc, SubPersonWithDesc).name.__delete__(self)


s3 = SubPersonWithDesc('Hyojoo')
# s3 = SubPersonWithDesc(9)
