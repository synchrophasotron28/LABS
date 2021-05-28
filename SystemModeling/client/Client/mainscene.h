#ifndef MAINSCENE_H
#define MAINSCENE_H

#include <QGLWidget>
#include <QMouseEvent>
#include <QtMath>
#include <QTimer>
#include <QTime>
#include <QDebug>
#include "http.h"

class MainScene:public QGLWidget
{
    Q_OBJECT
private:
    int currentHeight;
    int currentWidth;

    GLfloat xAxisRotation = 0;
    GLfloat yAxisRotation = 0;

    QPoint pressPosition;
    QTimer *timer;

    QString url = "http://127.0.0.1:5000/";
    HTTP http;

    // Размеры карты
    // =============================
    double beg_x = -10000;
    double end_x = 10000;
    double beg_y = -10000;
    double end_y = 10000;
    double beg_z = -10000;
    double end_z = 10000;
    // =============================


    float x=0;
    float y=0;
    float z=0;
    float t=0;
    unsigned int rendering_delay_ms = 50;
public:
    MainScene();

    void mousePressEvent(QMouseEvent *event) override;
    void mouseMoveEvent(QMouseEvent *event) override;

    void initializeGL() override;
    void resizeGL(int w, int h) override;
    void paintGL() override;

    void paintSphere(double radius, double X0, double Y0 ,double Z0, float red, float green, float blue);

    void GenerateTextures();

public slots:
    void TimerAlarm();
};

#endif // MAINSCENE_H
