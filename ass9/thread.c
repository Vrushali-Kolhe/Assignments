#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>	//for using sleep 
#include<pthread.h>
#include<time.h>	//for calculating time

void *f1(void *var){
	time_t rawtime;
	struct tm * timeinfo;
	time(&rawtime);
	timeinfo = localtime(&rawtime);
	sleep(1);				//to get proper output sleep thread 
	printf("%d:",timeinfo->tm_hour);	//output hour  
	return NULL;
}

void *f2(void *var){
	time_t rawtime;
	struct tm * timeinfo;
	time(&rawtime);
	timeinfo = localtime(&rawtime);
	sleep(2);                               //to get proper output
	printf("%d:",timeinfo->tm_min);		//output min
	return NULL;
}

void *f3(void *var){
	time_t rawtime;
	struct tm * timeinfo;
	time(&rawtime);
	timeinfo = localtime(&rawtime);
	sleep(3);                               //to get proper output
	printf("%d\n",timeinfo->tm_sec);	//output sec
	return NULL;
}

int main(){
	pthread_t t1_id, t2_id, t3_id;
	printf("Current time is: ");
	pthread_create(&t1_id, NULL, f1, NULL);		//thread to get hour
	pthread_create(&t2_id, NULL, f2, NULL);		//thread to get min
	pthread_create(&t3_id, NULL, f3, NULL);		//thread to get sec
	pthread_join(t1_id, NULL);
	pthread_join(t2_id, NULL);
	pthread_join(t3_id, NULL); 
	return 0;
}
