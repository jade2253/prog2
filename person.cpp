#include <cstdlib>
// Person class 

class Person{
	public:
		Person(int);
		int get();
		void set(int);
		int fibhelp();

	private:
		int age;
		int fib(int);
	};
 
Person::Person(int n){
	age = n;
	}
 
int Person::get(){
	return age;
	}
int Person::fib(int n){
	if (n <= 1)
		return n;
	return fib(n-1) + fib(n-2);
	}

void Person::set(int n){
	age = n;
	}

int Person::fibhelp(){
	return fib(age);
	}

extern "C"{
	Person* Person_new(int n) {return new Person(n);}
	int Person_get(Person* person) {return person->get();}
	void Person_set(Person* person, int n) {person->set(n);}
	int Person_fibhelp(Person* person) {return person->set(n);}
	void Person_delete(Person* person){
		if (person){
			delete person;
			person = nullptr;
			}
		}
	}