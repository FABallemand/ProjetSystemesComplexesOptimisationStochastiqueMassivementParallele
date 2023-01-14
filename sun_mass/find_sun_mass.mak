

UNAME := $(shell uname)

ifeq ($(shell uname -o 2>/dev/null),Msys)
	OS := MINGW
endif

ifneq ("$(OS)","")
	EZ_PATH=../../
endif

find_sun_massLIB_PATH=$(EZ_PATH)/libeasea/

CXXFLAGS =  -std=c++14 -fopenmp -O2 -g -Wall -fmessage-length=0 -I$(find_sun_massLIB_PATH)include

OBJS = find_sun_mass.o find_sun_massIndividual.o 

LIBS = -lpthread -fopenmp 
ifneq ("$(OS)","")
	LIBS += -lws2_32 -lwinmm -L"C:\MinGW\lib"
endif

#USER MAKEFILE OPTIONS :


#END OF USER MAKEFILE OPTIONS

TARGET =	find_sun_mass

$(TARGET):	$(OBJS)
	$(CXX) -o $(TARGET) $(OBJS) $(LDFLAGS) -g $(find_sun_massLIB_PATH)/libeasea.a $(LIBS)

	
#%.o:%.cpp
#	$(CXX) -c $(CXXFLAGS) $^

all:	$(TARGET)
clean:
ifneq ("$(OS)","")
	-del $(OBJS) $(TARGET).exe
else
	rm -f $(OBJS) $(TARGET)
endif
easeaclean:
ifneq ("$(OS)","")
	-del $(TARGET).exe *.o *.cpp *.hpp find_sun_mass.png find_sun_mass.dat find_sun_mass.prm find_sun_mass.mak Makefile find_sun_mass.vcproj find_sun_mass.csv find_sun_mass.r find_sun_mass.plot find_sun_mass.pop
else
	rm -f $(TARGET) *.o *.cpp *.hpp find_sun_mass.png find_sun_mass.dat find_sun_mass.prm find_sun_mass.mak Makefile find_sun_mass.vcproj find_sun_mass.csv find_sun_mass.r find_sun_mass.plot find_sun_mass.pop
endif

