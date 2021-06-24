#include "mainscene.h"

MainScene::MainScene()
{
    _proectionType = Default;
    timer = new QTimer;
    connect(timer, &QTimer::timeout, this, &MainScene::TimerAlarm);
    timer->start(rendering_delay_ms);
}

MainScene::MainScene(ProectionType type):_proectionType(type)
{

}

void MainScene::mousePressEvent(QMouseEvent *event)
{
    pressPosition = event->pos();
}

void MainScene::mouseMoveEvent(QMouseEvent *event)
{
    xAxisRotation += (180 * ((GLfloat)event->y() - (GLfloat)pressPosition.y())) / (currentHeight);
    yAxisRotation += (180 * ((GLfloat)event->x() - (GLfloat)pressPosition.x())) / (currentWidth);

    pressPosition = event->pos();
    updateGL();
}

void MainScene::initializeGL()
{
    glClearColor(1.0, 1.0, 1.0, 1.0);
    glClearColor(0.0, 0.0, 0.0, 1.0);
    glEnableClientState(GL_VERTEX_ARRAY);
    glEnableClientState(GL_COLOR_ARRAY);

    glShadeModel(GL_FLAT);
    glEnable(GL_CULL_FACE);
}

void MainScene::resizeGL(int w, int h)
{
    currentHeight = h;
    currentWidth = w;
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    //    glOrtho(-20.0, 20.0, -20.0, 20.0, -20.0, 20.0);
    glOrtho(beg_x, end_x, beg_y, end_y, beg_z, end_z);
    glViewport(0, 0, (GLint)w, (GLint)h);
    glMatrixMode(GL_MODELVIEW);
}

void MainScene::paintGL()
{
    //    glClear(GL_COLOR_BUFFER_BIT);

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
    glRotatef(yAxisRotation, 0.0, 1.0, 0.0);
    glRotatef(xAxisRotation, 1.0, 0.0, 0.0);
    //   glClear(GL_COLOR_BUFFER_BIT);

    double lineWidth = 3;

    // ОСЬ Х
    // ==============================================
    //    glColor3f(158/255.0, 164/255.0, 254/255.0);
    glColor3f(102/255.0, 204/255.0, 255/255.0);
    glLineWidth(lineWidth);
    glBegin(GL_LINE_STRIP);
    glVertex3f(beg_x, 0, 0);
    glVertex3f(end_x, 0, 0);
    glEnd();
    // ==============================================

    // ОСЬ Y
    // ==============================================
    glColor3f(1, 1, 0);
    glLineWidth(lineWidth);
    glBegin(GL_LINE_STRIP);
    glVertex3f(0, beg_y, 0);
    glVertex3f(0, end_y, 0);
    glEnd();
    // ==============================================

    // ОСЬ Z
    // ==============================================
    glColor3f(0, 1, 1);
    glLineWidth(lineWidth);
    glBegin(GL_LINE_STRIP);
    glVertex3f(0, 0, beg_z);
    glVertex3f(0, 0, end_z);
    glEnd();
    // ==============================================

    if (_proectionType == Default)
    {
        paintSphere(6371,0,0,0, 0, 204/255.0, 0);

        auto fo = http.get_space_objects();
        for (int i=0; i<fo.size(); i++)
        {
            if (i%2 == 0)
                paintSphere(300,fo[i].x , fo[i].y, fo[i].z, 1, 0, 0);
            else
                paintSphere(300,fo[i].x , fo[i].y, fo[i].z, 0, 0, 1);
        }
    }
    else
    {
        auto fo = http.get_space_objects();
        for (int i=0; i<fo.size(); i++)
        {
            switch (_proectionType) {
            case XOY:
            {
                if (i % 2 == 0)
                    paintSphere(300,fo[i].x , fo[i].y, 0, 1, 0, 0);
                else
                    paintSphere(300,fo[i].x , fo[i].y, 0, 0, 0, 1);
                break;
            }

            case XOZ:
            {
                if (i % 2 == 0)
                    paintSphere(300,fo[i].x , fo[i].z, 0, 1, 0, 0);
                else
                    paintSphere(300,fo[i].x , fo[i].z, 0, 0, 0, 1);
                break;
            }

            case YOZ:
            {
                if (i % 2 == 0)
                    paintSphere(300,fo[i].y , fo[i].z, 0, 1, 0, 0);
                else
                    paintSphere(300,fo[i].y , fo[i].z, 0, 0, 0, 1);
                break;
            }

            }

        }
    }




}

void MainScene::paintSphere(double radius, double X0, double Y0 ,double Z0, float red, float green, float blue)
{
    glColor3f(red, green, blue);

    float x,y,z;
    float X=-M_PI,Y=0;
    float Z=0;
    float step = 0.1f;
    glBegin(GL_TRIANGLE_STRIP);

    while(X<M_PI)
    {
        while(Y<2*M_PI)
        {
            x=radius*cos(X)*cos(Y);
            y=radius*cos(X)*sin(Y);
            z=radius*sin(X);
            glVertex3f(X0+x,Y0+y,Z0+z);

            x=radius*cos(X)*cos(Y);
            y=radius*cos(X+step)*sin(Y);
            z=radius*sin(X);
            glVertex3f(X0+x,Y0+y,Z0+z);

            x=radius*cos(X+step)*cos(Y);
            y=radius*cos(X)*sin(Y);
            z=radius*sin(X+step);
            glVertex3f(X0+x,Y0+y,Z0+z);
            Y+=step;
        }
        Y=0;
        X+=step;
    }
    glEnd();
}

void MainScene::GenerateTextures()
{

}

void MainScene::TimerAlarm()
{
    http.send_request(url);


    paintGL();
    updateGL();
}

void MainScene::SetSpaceObjectList(QList<SpaceObject> list)
{
    http.set_space_objects(list);
    paintGL();
    updateGL();
}

