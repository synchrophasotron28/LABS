
#include "mainscene.h"
#include <QApplication>
#include <mainwindow.h>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    MainWindow w;
    w.show();
//    MainScene scene;
//    scene.resize(700, 700);
//    scene.show();

    return a.exec();
}
