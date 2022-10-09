#include<iostream>
#include<fstream>
#include<iomanip>
#include<unistd.h>
#include<cstdio>
#include<cstring>
using namespace std;
class Student
{
	private:
		int roll;
		char name[30];
		int logic;
		int dsa;
		int oops;
		int math;
		float per;
		char grade;
		int total;
	public:
		void getdata();
		void showdata();
		void calculate();
		int rollnum();
		int returnTotal();
		void tabular();
		int returnOOPS();
		int returnDSA();
		int returnMath();
		int returnLogic();
		char returnGrade();
};
char Student ::returnGrade()
{
	return grade;
}
int Student :: rollnum()
{
	return roll;
}
int Student :: returnOOPS()
{
	return oops;
}
int Student :: returnDSA()
{
	return dsa;
}
int Student :: returnMath()
{
	return math;
}
int Student :: returnLogic()
{
	return logic;
}
int Student :: returnTotal()
{
	return total;
}
void Student :: getdata()
{
	system("clear");
	cout<<"\nEnter roll number:";
	cin>>roll;
	cout<<"\nEnter name of student:";
	cin.ignore();//The cin.ignore() function is used which is used to ignore or clear one or more characters from the input buffer.
	cin.getline(name,30);
	cout<<"\nEnter marks of Digital Logic:";
	cin>>logic;
	cout<<"\nEnter marks of Data Structure:";
	cin>>dsa;
	cout<<"\nEnter marks of Math:";
	cin>>math;
	cout<<"\nEnter marks of OOPS:";
	cin>>oops;
	calculate();
}
void Student :: tabular()
{
	cout<<setw(2)<<setfill(' ')<<roll;
	cout<<setw(14)<<setfill(' ')<<name;
	cout<<setw(12)<<setfill(' ')<<logic;
	cout<<setw(10)<<setfill(' ')<<dsa;
	cout<<setw(6)<<setfill(' ')<<math;
	cout<<setw(8)<<setfill(' ')<<oops;
	cout<<setw(8)<<setfill(' ')<<grade;
	cout<<setw(14)<<setfill(' ')<<per;
	cout<<setw(8)<<setfill(' ')<<total<<endl;
}

void Student :: showdata()
{
	system("clear");
	cout<<"\nRoll number:"<<roll;
	cout<<"\nName of student:"<<name;
	cout<<"\nMarks of Digital Logic:"<<logic;
	cout<<"\nMarks of Data Structure:"<<dsa;
	cout<<"\nMarks of Math:"<<math;
	cout<<"\nMarks of OOPS:"<<oops;
	cout<<"\nGrade:"<<grade;
	cout<<"\nTotal marks:"<<total;
	cout<<"\nPercentage:"<<per;
	cout<<endl;
}
void Student :: calculate()
{
	total=logic+dsa+math+oops;
	per=total/4.0;
	if(per>70)
	{
		grade='A';
	}
	else if (per>60)
	{
		grade='B';
	}
	else if (per>50)
	{
		grade='C';
	}
	else if (per>40)
	{
		grade='D';
	}
	else if (per>30)
	{
		grade='E';
	}
	else
	{
		grade='F';
	}
}
void create_student()
{
	system("clear");
	char opt;
	Student s;
	ofstream outfile;
	outfile.open("student.dat", ios::app | ios::binary);
	s.getdata();
	outfile.write((char*) &s,sizeof(s));
	outfile.close();
	cout<<"\nPress y for adding more data and n for not adding the data\n";
	cin>>opt;
	if(opt=='y' || opt=='Y')

	{
		create_student();
	}
	else
	{
		cout<<"\nExisting from creating student record\n";
	}
	cin.ignore();
	cout<<"Press any key to continue\n";
	getchar();
	system("clear");
}
void AccGrade(char grade)
{
	system("clear");
	Student s;
	int c=0;
	ifstream infile;
	infile.open("student.dat",ios::binary);
	cout<<"Students of grade:"<<grade<<endl;
	cout<<"===========================================================================================\n";
	cout<<"R.No       Name        Dig. Logic   DSA   Math   OOPS    Grade   Percentage   Total"<<endl;
	cout<<"===========================================================================================\n";
	while(infile.read((char*) &s,sizeof(s)))
	{
		if(s.returnGrade()==grade)
		{
			s.tabular();
			c++;
		}
	}
	if(c==0)
	{
		sleep(2);
		cout<<"\n\n\n\t\t\t\tOOPS Nothing Found\n";
	}
	cin.ignore();
	cout<<"Press any key to continue\n";

	getchar();
	system("clear");
}
void subject_mean()
{
	system("clear");
	int ctr=0;
	float oops_mean=0,dsa_mean=0,math_mean=0,logic_mean=0;
	system("clear");
	Student s;
	ifstream infile;
	infile.open("student.dat",ios::binary);
	if(!infile)
	{
		cout<<"File can't link !!!";
	}
	else
	{
		while(infile.read((char*) &s,sizeof(s)))
		{
			ctr++;
			oops_mean=oops_mean+s.returnOOPS();
			math_mean=math_mean+s.returnMath();
			dsa_mean=dsa_mean+s.returnDSA();
			logic_mean=logic_mean+s.returnLogic();
		}
		oops_mean/=ctr;
		math_mean/=ctr;
		dsa_mean/=ctr;
		logic_mean/=ctr;
		cout<<"\nOOPS mean:"<<oops_mean;
		cout<<"\nMath mean:"<<math_mean;
		cout<<"\nDSA mean:"<<dsa_mean;
		cout<<"\nDigital Logic mean:"<<logic_mean;
	}
	cin.ignore();
	cout<<"\nPress any key to continue\n";
	getchar();
	system("clear");
}
void class_result()
{
	int ch;
	system("clear");
	Student s;
	ifstream inFile;
	inFile.open("student.dat",ios::binary);
	if(!inFile)
	{
		cout<<"File could not be open!!!";
	}
	cout<<"\n\n\t\tALL STUDENTS RESULT \n\n";
	cout<<"===========================================================================================\n";
	cout<<"R.No       Name        Dig. Logic   DSA   Math   OOPS    Grade   Percentage   Total"<<endl;
	cout<<"===========================================================================================\n";
	while(inFile.read((char*) &s, sizeof(s)))
	{
		s.tabular();		
	}
	cout<<"=============================================================================================\n";
	inFile.close();
	cin.ignore();
	cout<<"Press any key to continue\n";
	getchar();
	system("clear");
}
void update_student()
{
     Student s;
     ifstream infile("student.dat");
     ofstream outfile("new.dat",ios::binary);
     int roll,flag=0;
     if(!infile)
     {
         cout<<"\nFile not found";
     }
     else
     {   
         cout<<"\nEnter roll number of the student: ";
         cin>>roll;
         system("cls");
         while(infile.read((char*)&s,sizeof(s)))
         {
             if(roll==s.rollnum())
             {
                 cout<<"\nEnter new details";
                 s.getdata();
                 
                 outfile.write((char*)&s,sizeof(s));
                 flag=1;
             }
             else
             { 
                 outfile.write((char*)&s,sizeof(s));
             }
         }
         if(flag==0)
         {
             cout<<"\nRecord not found";
         }
     }
     infile.close();
     outfile.close();
     remove("student.dat");
     rename("new.dat","student.dat");
     cin.ignore();
     cout<<"Press any key to continue\n";
	getchar();
	system("clear");
}
void display()
{
	system("clear");
	Student s;
	ifstream infile;
	infile.open("student.dat",ios::binary);
	if(!infile)
	{
		cout<<"File does not exist\n";
	}
	else
	{
		cout<<"All student record.....\n";
		while(infile.read((char*) &s,sizeof(s)))
		{
			getchar();
			s.showdata();
		}
		infile.close();
	}
	cin.ignore();
	cout<<"Press any key to continue\n";
	getchar();
	system("clear");
}
void class_mean()
{
	system("clear");
	float mean=0.0;
	int ctr=0;
	float Tmean=0.0;
	ifstream infile; 
	Student s;
	infile.open("student.dat",ios::binary);
	if(!infile)
	{
		cout<<"File can't link\n";
	}
	else
	{
		while(infile.read((char*) &s,sizeof(s)))
		{
			mean=mean+(s.returnTotal()/4.0);
			ctr++;
		}
		Tmean=(float)mean/ctr;
		cout<<"\nClass mean is:"<<Tmean;
	}
	cin.ignore();
	cout<<"Press any key to continue\n";
	getchar();
	system("clear");
}
void delete_student()
{	
	int opt;
	int roll;
	system("clear");
	cout<<"Enter roll number:";
	cin>>roll;
	Student s;
	ifstream infile;
	infile.open("student.dat",ios::binary);
	if(!infile)
	{
		cout<<"\nFile can't link";
	}
	else
	{
		ofstream outfile;
		outfile.open("new.dat",ios::out);
		while(infile.read((char*) &s,sizeof(s)))
		{
			if(s.rollnum() != roll)
			{
				outfile.write((char*) &s,sizeof(s));
			}
		}
		infile.close();
		outfile.close();
		remove("student.dat");
		rename("new.dat","student.dat");
		cout<<"\nRecord deleted";
		cout<<"\nPress y for deleting more data and n for not deleting the data\n";
		cin>>opt;
		if(opt=='y' || opt=='Y')
		{
			delete_student();
		}
		else
		{
			cout<<"\nExisting........\n";
		}
	}
	cin.ignore();
	cout<<"Press any key to continue\n";
	getchar();
	system("clear");
}
void search_disp()
{
	int roll;
	system("clear");
	cout<<"Enter roll number:";
	cin>>roll;
	Student s;
	ifstream infile;
	infile.open("student.dat",ios::binary);
	if(!infile)
	{
		cout<<"File does not exist\n";
	}
	else
	{
		int ctr=0;
		while(infile.read((char*) &s,sizeof(s)))
		{
			if(s.rollnum() == roll)
			{
				cout<<"\nRecord founded...";
				cout<<"\n...Press any key to see the record...\n";
				getchar();
				s.showdata();
				ctr++;
				infile.close();
				break;
			}
		}
		if(ctr==0)
		{
			cout<<"\n\nRecord not found\n";
		}
	}
	cin.ignore();
	cout<<"Press any key to continue\n";
	getchar();
	system("clear");
}
int Password()
{
     char pass[8];
     pass[7]='\0';
     int t=0;
     start:
     system("clear");
     cout<<"\nEnter the password(7 characters) :";
     for(int i=0;i<7;++i)
     {
             pass[i]=getchar();
     }
     if(strcmp(pass,"Saurabh")==0)
     {
        cout<<"\nACCESS GRANTED\n";
        cin.ignore();
        cout<<"Press any key to continue\n";
		getchar();
		system("clear");
        return 1;
     }
     else
     {
         if(t==2)
         {
             cout<<"\nACCESS DENIED";
             return 0;
         }
         cout<<"\nTRY AGAIN\n";
         ++t;
         sleep(2);
         goto start;
     }
}

int main()
{
	char grade;
	int opt,num;
	cout<<"\t\t\t\t\t\t\t\t====================================================================================\n";
	cout<<"\t\t\t\t\t\t\t\t\t\t\tTHIS IS STUDENT REPORT CARD MANEGEMENT SYSTEM"<<endl;
	sleep(2);
	cout<<"\n\n\t\t\t\t\t\t\t\t\t\t\tMade by:Saurabh Kaperwan"<<endl;
	cout<<"\t\t\t\t\t\t\t\t======================================================================================\n";
	sleep(4);
	system("clear");
	if(Password()==1)
	{
		do
		{
			cout<<"\n These are your option:";
			cout<<"\n=======================================================================";
			cout<<"\n0.To exit\n";
			cout<<"1.To create a record\n";
			cout<<"2.To delete a record\n";
			cout<<"3.To read all records from file\n";
			cout<<"4.To Search a record\n";
			cout<<"5.Class mean\n";	
			cout<<"6.Display all students record in tabular form\n";
			cout<<"7.To show the result of particular grade\n";
			cout<<"8.All Subject Mean\n";
			cout<<"9.Modify student record\n";
			cout<<"=========================================================================\n";
			sleep(2);
			cout<<"\nPlese Enter your option:";
			cin>>opt;
			switch(opt)
			{
				case 0:
					cout<<"\nLeaving thank you!!\n";
					break;
				case 1:
					create_student();
					break;
				case 2:
					delete_student();
					break;
				case 3:
					display();
					break;
				case 4:
					search_disp();
					break;
				case 5:
					class_mean();
					break;
				case 6:
					class_result();
					break;
				case 7:
					cout<<"Enter Grade:";
					cin>>grade;
			 		AccGrade(grade);
			 		break;
			 	case 8:
			 		subject_mean();
			 		break;
			 	case 9:
			 		update_student();
			 		break;
				default:
					cout<<"Invalid choice";
			}	
		}while(opt!=0);
	}
}
//setw() helps you defined the width of the output
//setfill() Fill the rest with the character you want 
