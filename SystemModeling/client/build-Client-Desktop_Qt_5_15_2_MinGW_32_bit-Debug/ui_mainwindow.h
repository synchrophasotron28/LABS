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
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QSplitter>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QTableWidget>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *centralwidget;
    QGridLayout *gridLayout_5;
    QSplitter *splitter_3;
    QSplitter *splitter;
    QWidget *SideWidget;
    QGridLayout *gridLayout_2;
    QTableWidget *SpaceObjectTable;
    QWidget *gridLayoutWidget;
    QGridLayout *OpenglLayout;
    QSplitter *splitter_2;
    QWidget *widget;
    QVBoxLayout *verticalLayout;
    QWidget *widget_2;
    QGridLayout *gridLayout;
    QLabel *label;
    QHBoxLayout *XoyOpenGlWidgetLayout;
    QWidget *widget_3;
    QVBoxLayout *verticalLayout_2;
    QWidget *widget_4;
    QGridLayout *gridLayout_3;
    QLabel *label_2;
    QHBoxLayout *XozOpenGlWidgetLayout;
    QWidget *widget_5;
    QVBoxLayout *verticalLayout_3;
    QWidget *widget_6;
    QGridLayout *gridLayout_4;
    QLabel *label_3;
    QHBoxLayout *YozOpenGlWidgetLayout;
    QMenuBar *menubar;
    QStatusBar *statusbar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QString::fromUtf8("MainWindow"));
        MainWindow->resize(963, 736);
        centralwidget = new QWidget(MainWindow);
        centralwidget->setObjectName(QString::fromUtf8("centralwidget"));
        gridLayout_5 = new QGridLayout(centralwidget);
        gridLayout_5->setObjectName(QString::fromUtf8("gridLayout_5"));
        splitter_3 = new QSplitter(centralwidget);
        splitter_3->setObjectName(QString::fromUtf8("splitter_3"));
        splitter_3->setOrientation(Qt::Vertical);
        splitter = new QSplitter(splitter_3);
        splitter->setObjectName(QString::fromUtf8("splitter"));
        splitter->setOrientation(Qt::Horizontal);
        SideWidget = new QWidget(splitter);
        SideWidget->setObjectName(QString::fromUtf8("SideWidget"));
        SideWidget->setStyleSheet(QString::fromUtf8(""));
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
        SpaceObjectTable->setStyleSheet(QString::fromUtf8("/*QHeaderView::section {\n"
"    background-color: #646464;\n"
"    padding: 4px;\n"
"    font-size: 14pt;\n"
"    border-style: none;\n"
"    border-bottom: 1px solid #fffff8;\n"
"    border-right: 1px solid #fffff8;\n"
"}\n"
"\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border-top: 1px solid #fffff8;\n"
"}\n"
"\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border-left: 1px solid #fffff8;\n"
"}\n"
"*/\n"
"\n"
"QHeaderView::section {\n"
"       background-color: #DAF2F7;\n"
"       padding: 4px;\n"
"	   color: #2c3e50;\n"
"       border: 0px solid #fffff8;\n"
"       font-size: 10pt;\n"
"}\n"
"\n"
"QTableCornerButton::section {\n"
"       background-color: #DAF2F7;\n"
"       border: 0px solid #fffff8;\n"
"}\n"
"\n"
"QTableWidget {\n"
"       gridline-color: #fffff8;\n"
"	   border: 0px solid #fffff8;\n"
"       font-size: 12pt;\n"
"\n"
"		/*selection-background-color:#52b3d9;*/\n"
"		selection-background-color:#a4cad9;\n"
"		selection-color:#1f3a93;\n"
"}\n"
"\n"
"\n"
"QWidget {\n"
"       background-"
                        "color: #e4f1fe;\n"
"       color: #2c3e50;	 \n"
"}\n"
" \n"
"\n"
"\n"
"QTableView\n"
"{\n"
"  alternate-background-color: yellow;\n"
"}\n"
"\n"
" QTreeView {\n"
"     alternate-background-color: yellow;\n"
"     show-decoration-selected: 1;\n"
" }\n"
"\n"
"\n"
" QTreeView::item {\n"
"      border: 1px solid #d9d9d9;\n"
"     border-top-color: transparent;\n"
"     border-bottom-color: transparent;\n"
" }\n"
"\n"
" QTreeView::item:hover {\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #e7effd, stop: 1 #cbdaf1);\n"
"     border: 1px solid #bfcde4;\n"
" }\n"
"\n"
" QTreeView::item:selected {\n"
"     border: 1px solid #567dbc;\n"
" }\n"
"\n"
" QTreeView::item:selected:active{\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #6ea1f1, stop: 1 #567dbc);\n"
" }\n"
"\n"
" QTreeView::item:selected:!active {\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #6b9be8, stop: 1 #577fbf);\n"
" }\n"
""));
        SpaceObjectTable->setShowGrid(true);
        SpaceObjectTable->horizontalHeader()->setVisible(true);
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
        splitter_3->addWidget(splitter);
        splitter_2 = new QSplitter(splitter_3);
        splitter_2->setObjectName(QString::fromUtf8("splitter_2"));
        splitter_2->setOrientation(Qt::Horizontal);
        widget = new QWidget(splitter_2);
        widget->setObjectName(QString::fromUtf8("widget"));
        verticalLayout = new QVBoxLayout(widget);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        widget_2 = new QWidget(widget);
        widget_2->setObjectName(QString::fromUtf8("widget_2"));
        widget_2->setMaximumSize(QSize(16777215, 20));
        gridLayout = new QGridLayout(widget_2);
        gridLayout->setSpacing(0);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        gridLayout->setContentsMargins(0, 0, 0, 0);
        label = new QLabel(widget_2);
        label->setObjectName(QString::fromUtf8("label"));
        label->setAlignment(Qt::AlignCenter);

        gridLayout->addWidget(label, 0, 0, 1, 1);


        verticalLayout->addWidget(widget_2);

        XoyOpenGlWidgetLayout = new QHBoxLayout();
        XoyOpenGlWidgetLayout->setSpacing(0);
        XoyOpenGlWidgetLayout->setObjectName(QString::fromUtf8("XoyOpenGlWidgetLayout"));

        verticalLayout->addLayout(XoyOpenGlWidgetLayout);

        splitter_2->addWidget(widget);
        widget_3 = new QWidget(splitter_2);
        widget_3->setObjectName(QString::fromUtf8("widget_3"));
        verticalLayout_2 = new QVBoxLayout(widget_3);
        verticalLayout_2->setObjectName(QString::fromUtf8("verticalLayout_2"));
        widget_4 = new QWidget(widget_3);
        widget_4->setObjectName(QString::fromUtf8("widget_4"));
        widget_4->setMaximumSize(QSize(16777215, 20));
        gridLayout_3 = new QGridLayout(widget_4);
        gridLayout_3->setSpacing(0);
        gridLayout_3->setObjectName(QString::fromUtf8("gridLayout_3"));
        gridLayout_3->setContentsMargins(0, 0, 0, 0);
        label_2 = new QLabel(widget_4);
        label_2->setObjectName(QString::fromUtf8("label_2"));
        label_2->setAlignment(Qt::AlignCenter);

        gridLayout_3->addWidget(label_2, 0, 0, 1, 1);


        verticalLayout_2->addWidget(widget_4);

        XozOpenGlWidgetLayout = new QHBoxLayout();
        XozOpenGlWidgetLayout->setSpacing(0);
        XozOpenGlWidgetLayout->setObjectName(QString::fromUtf8("XozOpenGlWidgetLayout"));

        verticalLayout_2->addLayout(XozOpenGlWidgetLayout);

        splitter_2->addWidget(widget_3);
        widget_5 = new QWidget(splitter_2);
        widget_5->setObjectName(QString::fromUtf8("widget_5"));
        verticalLayout_3 = new QVBoxLayout(widget_5);
        verticalLayout_3->setObjectName(QString::fromUtf8("verticalLayout_3"));
        widget_6 = new QWidget(widget_5);
        widget_6->setObjectName(QString::fromUtf8("widget_6"));
        widget_6->setMaximumSize(QSize(16777215, 20));
        gridLayout_4 = new QGridLayout(widget_6);
        gridLayout_4->setSpacing(0);
        gridLayout_4->setObjectName(QString::fromUtf8("gridLayout_4"));
        gridLayout_4->setContentsMargins(0, 0, 0, 0);
        label_3 = new QLabel(widget_6);
        label_3->setObjectName(QString::fromUtf8("label_3"));
        label_3->setAlignment(Qt::AlignCenter);

        gridLayout_4->addWidget(label_3, 0, 0, 1, 1);


        verticalLayout_3->addWidget(widget_6);

        YozOpenGlWidgetLayout = new QHBoxLayout();
        YozOpenGlWidgetLayout->setSpacing(0);
        YozOpenGlWidgetLayout->setObjectName(QString::fromUtf8("YozOpenGlWidgetLayout"));

        verticalLayout_3->addLayout(YozOpenGlWidgetLayout);

        splitter_2->addWidget(widget_5);
        splitter_3->addWidget(splitter_2);

        gridLayout_5->addWidget(splitter_3, 0, 0, 1, 1);

        MainWindow->setCentralWidget(centralwidget);
        menubar = new QMenuBar(MainWindow);
        menubar->setObjectName(QString::fromUtf8("menubar"));
        menubar->setGeometry(QRect(0, 0, 963, 30));
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
        label->setText(QCoreApplication::translate("MainWindow", "XOY", nullptr));
        label_2->setText(QCoreApplication::translate("MainWindow", "XOZ", nullptr));
        label_3->setText(QCoreApplication::translate("MainWindow", "YOZ", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
