/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created by: Qt User Interface Compiler version 5.15.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QSplitter>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QTableWidget>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *centralwidget;
    QGridLayout *gridLayout;
    QSplitter *splitter;
    QWidget *SideWidget;
    QGridLayout *gridLayout_2;
    QTableWidget *SpaceObjectTable;
    QWidget *gridLayoutWidget;
    QGridLayout *OpenglLayout;
    QMenuBar *menubar;
    QStatusBar *statusbar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QString::fromUtf8("MainWindow"));
        MainWindow->resize(800, 600);
        centralwidget = new QWidget(MainWindow);
        centralwidget->setObjectName(QString::fromUtf8("centralwidget"));
        gridLayout = new QGridLayout(centralwidget);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        splitter = new QSplitter(centralwidget);
        splitter->setObjectName(QString::fromUtf8("splitter"));
        splitter->setOrientation(Qt::Horizontal);
        SideWidget = new QWidget(splitter);
        SideWidget->setObjectName(QString::fromUtf8("SideWidget"));
        SideWidget->setStyleSheet(QString::fromUtf8("background-color: rgb(255, 136, 0);"));
        gridLayout_2 = new QGridLayout(SideWidget);
        gridLayout_2->setObjectName(QString::fromUtf8("gridLayout_2"));
        SpaceObjectTable = new QTableWidget(SideWidget);
        if (SpaceObjectTable->columnCount() < 2)
            SpaceObjectTable->setColumnCount(2);
        QTableWidgetItem *__qtablewidgetitem = new QTableWidgetItem();
        SpaceObjectTable->setHorizontalHeaderItem(0, __qtablewidgetitem);
        QTableWidgetItem *__qtablewidgetitem1 = new QTableWidgetItem();
        SpaceObjectTable->setHorizontalHeaderItem(1, __qtablewidgetitem1);
        if (SpaceObjectTable->rowCount() < 2)
            SpaceObjectTable->setRowCount(2);
        QTableWidgetItem *__qtablewidgetitem2 = new QTableWidgetItem();
        SpaceObjectTable->setVerticalHeaderItem(0, __qtablewidgetitem2);
        QTableWidgetItem *__qtablewidgetitem3 = new QTableWidgetItem();
        SpaceObjectTable->setVerticalHeaderItem(1, __qtablewidgetitem3);
        SpaceObjectTable->setObjectName(QString::fromUtf8("SpaceObjectTable"));
        SpaceObjectTable->setShowGrid(true);
        SpaceObjectTable->horizontalHeader()->setVisible(false);
        SpaceObjectTable->horizontalHeader()->setHighlightSections(true);
        SpaceObjectTable->verticalHeader()->setVisible(false);

        gridLayout_2->addWidget(SpaceObjectTable, 0, 0, 1, 1);

        splitter->addWidget(SideWidget);
        gridLayoutWidget = new QWidget(splitter);
        gridLayoutWidget->setObjectName(QString::fromUtf8("gridLayoutWidget"));
        OpenglLayout = new QGridLayout(gridLayoutWidget);
        OpenglLayout->setObjectName(QString::fromUtf8("OpenglLayout"));
        OpenglLayout->setContentsMargins(0, 0, 0, 0);
        splitter->addWidget(gridLayoutWidget);

        gridLayout->addWidget(splitter, 0, 0, 1, 1);

        MainWindow->setCentralWidget(centralwidget);
        menubar = new QMenuBar(MainWindow);
        menubar->setObjectName(QString::fromUtf8("menubar"));
        menubar->setGeometry(QRect(0, 0, 800, 30));
        MainWindow->setMenuBar(menubar);
        statusbar = new QStatusBar(MainWindow);
        statusbar->setObjectName(QString::fromUtf8("statusbar"));
        MainWindow->setStatusBar(statusbar);

        retranslateUi(MainWindow);

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QCoreApplication::translate("MainWindow", "MainWindow", nullptr));
        QTableWidgetItem *___qtablewidgetitem = SpaceObjectTable->horizontalHeaderItem(0);
        ___qtablewidgetitem->setText(QCoreApplication::translate("MainWindow", "\320\235\320\276\320\262\321\213\320\271 \321\201\321\202\320\276\320\273\320\261\320\265\321\206", nullptr));
        QTableWidgetItem *___qtablewidgetitem1 = SpaceObjectTable->horizontalHeaderItem(1);
        ___qtablewidgetitem1->setText(QCoreApplication::translate("MainWindow", "\320\235\320\276\320\262\321\213\320\271 \321\201\321\202\320\276\320\273\320\261\320\265\321\206", nullptr));
        QTableWidgetItem *___qtablewidgetitem2 = SpaceObjectTable->verticalHeaderItem(0);
        ___qtablewidgetitem2->setText(QCoreApplication::translate("MainWindow", "\320\235\320\276\320\262\320\260\321\217 \321\201\321\202\321\200\320\276\320\272\320\260", nullptr));
        QTableWidgetItem *___qtablewidgetitem3 = SpaceObjectTable->verticalHeaderItem(1);
        ___qtablewidgetitem3->setText(QCoreApplication::translate("MainWindow", "\320\235\320\276\320\262\320\260\321\217 \321\201\321\202\321\200\320\276\320\272\320\260", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
