QT       += core gui opengl network
LIBS += -lglu32 -lopengl32
greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

CONFIG += c++11

#LIBS+=-lglut32
#LIBS+=-LpathToYourGLUTLib

# You can make your code fail to compile if it uses deprecated APIs.
# In order to do so, uncomment the following line.
#DEFINES += QT_DISABLE_DEPRECATED_BEFORE=0x060000    # disables all the APIs deprecated before Qt 6.0.0

SOURCES += \
    main.cpp \
    mainscene.cpp \
    http.cpp \
    mainwindow.cpp \
    spaceobject.cpp

HEADERS += \
    mainscene.h \
    mainwindow.h \
    spaceobject.h \
    http.h

FORMS += \
    mainwindow.ui

# Default rules for deployment.
qnx: target.path = /tmp/$${TARGET}/bin
else: unix:!android: target.path = /opt/$${TARGET}/bin
!isEmpty(target.path): INSTALLS += target
