#ifndef SPACEOBJECT_H
#define SPACEOBJECT_H

#include <QObject>
#include <QString>

class SpaceObject
{
public:
    explicit SpaceObject(QObject *parent = nullptr);
    explicit SpaceObject (QString name,double x, double y, double z,
                          double theta,
                          double h_p, double h_a,
                          double r, double p,
                          double OMEGA, double omega,
                          double e, double U,
                          double tau, double m, double i);
    QString name;

    // Параметры
    // ===========
    double x;
    double y;
    double z;
    double theta;
    double h_p;
    double h_a;
    double r;
    double p;
    double OMEGA;
    double omega;
    double e;
    double U;
    double tau;
    double m;
    double i;
    // ===========


};

#endif // SPACEOBJECT_H
