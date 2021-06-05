#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    InitTable();
    MainScene *scene = new MainScene;
    MainScene *xoy = new MainScene(XOY);
    MainScene *xoz = new MainScene(XOZ);
    MainScene *yoz = new MainScene(YOZ);

    scene->setMinimumWidth(300);

//SetSpaceObjectList
    connect(&scene->http, &HTTP::SpaceObjectListUpdated, this, &MainWindow::RenderSpaceObjectTable);

    connect(&scene->http, &HTTP::SpaceObjectListUpdated, xoy, &MainScene::SetSpaceObjectList);
    connect(&scene->http, &HTTP::SpaceObjectListUpdated, xoz, &MainScene::SetSpaceObjectList);
    connect(&scene->http, &HTTP::SpaceObjectListUpdated, yoz, &MainScene::SetSpaceObjectList);

    ui->OpenglLayout->addWidget(scene);

    ui->XoyOpenGlWidgetLayout->addWidget(xoy);
    ui->XozOpenGlWidgetLayout->addWidget(xoz);
    ui->YozOpenGlWidgetLayout->addWidget(yoz);
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::InitTable()
{
    QStringList horizontalHeaders;
    ui->SpaceObjectTable->setRowCount(0);
    ui->SpaceObjectTable->setColumnCount(0);

    ui->SpaceObjectTable->setColumnCount(16-3);

    horizontalHeaders << "Название";
    horizontalHeaders << "x";
    horizontalHeaders << "y";
    horizontalHeaders << "z";
    horizontalHeaders << "theta";
//    horizontalHeaders << "h_p";
//    horizontalHeaders << "h_a";
    horizontalHeaders << "r";
    horizontalHeaders << "p";
    horizontalHeaders << "OMEGA";
    horizontalHeaders << "omega";
    horizontalHeaders << "e";
//    horizontalHeaders << "U";
    horizontalHeaders << "Tau";
    horizontalHeaders << "m";
    horizontalHeaders << "i";

    ui->SpaceObjectTable->setHorizontalHeaderLabels(horizontalHeaders);
    ui->SpaceObjectTable->setRowCount(1);

//    ui->SpaceObjectTable->horizontalHeader()->setSectionResizeMode(QHeaderView::Stretch);
//    ui->SpaceObjectTable->horizontalHeader()->setSectionResizeMode(QHeaderView::ResizeMode::ResizeToContents);
}

void MainWindow::RenderSpaceObjectTable(QList<SpaceObject> list)
{
    // Установить кол-во строк
    ui->SpaceObjectTable->setRowCount(list.size());

    //Жирный шрифт
    QFont font;
    font.setBold(true);


    // Заполнение таблицы
    for (int i=0; i<list.size(); i++)
    {
        ui->SpaceObjectTable->setItem(i, 0, new QTableWidgetItem(list[i].name));
        ui->SpaceObjectTable->item(i,0)->setFont(font);
        ui->SpaceObjectTable->setItem(i, 1, new QTableWidgetItem(QString::number(list[i].x)));
        ui->SpaceObjectTable->setItem(i, 2, new QTableWidgetItem(QString::number(list[i].y)));
        ui->SpaceObjectTable->setItem(i, 3, new QTableWidgetItem(QString::number(list[i].z)));
        ui->SpaceObjectTable->setItem(i, 4, new QTableWidgetItem(QString::number(list[i].theta)));
//        ui->SpaceObjectTable->setItem(i, 5, new QTableWidgetItem(QString::number(list[i].h_p)));
//        ui->SpaceObjectTable->setItem(i, 6, new QTableWidgetItem(QString::number(list[i].h_a)));
        ui->SpaceObjectTable->setItem(i, 5, new QTableWidgetItem(QString::number(list[i].r)));
        ui->SpaceObjectTable->setItem(i, 6, new QTableWidgetItem(QString::number(list[i].p)));
        ui->SpaceObjectTable->setItem(i, 7, new QTableWidgetItem(QString::number(list[i].OMEGA)));
        ui->SpaceObjectTable->setItem(i, 8, new QTableWidgetItem(QString::number(list[i].omega)));
        ui->SpaceObjectTable->setItem(i, 9, new QTableWidgetItem(QString::number(list[i].e)));
//        ui->SpaceObjectTable->setItem(i, 12, new QTableWidgetItem(QString::number(list[i].U)));
        ui->SpaceObjectTable->setItem(i, 10, new QTableWidgetItem(QString::number(list[i].tau)));
        ui->SpaceObjectTable->setItem(i, 11, new QTableWidgetItem(QString::number(list[i].m)));
        ui->SpaceObjectTable->setItem(i, 12, new QTableWidgetItem(QString::number(list[i].i)));
    }
}
