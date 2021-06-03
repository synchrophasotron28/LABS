#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <mainscene.h>
#include <QSplitter>


namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private:
    Ui::MainWindow *ui;
    void InitTable();

public slots:
    void RenderSpaceObjectTable(QList<SpaceObject> list);

};

#endif // MAINWINDOW_H
