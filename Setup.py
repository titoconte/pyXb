
import numpy as np
from datetime import datetime
import os

class XbParms():

    def __init__():

        self._advection=True
        self._avalanching=True
        self._bchwiz=False
        self._cyclic=False
        self._flow=True
        self._gwflow=False
        self._lwave=True
        self._morphology=True
        self._nonh=False
        self._q3d=False
        self._sedtrans=True
        self._setbathy=False
        self._ships=False
        self._single_dir=False
        self._snells=False
        self._swave=True
        self._swrunup=False
        self._vegetation=False
        self._viscosity=True
        self._wavemodel='surfbeat'
        self._wind=False

    def DirectionalResolution(
            self,
            thetanaut=True,
            thetamin=90,
            thetamax=90,
            dtheta=10,
            dtheta_s=10
        ):

        self._thetamin = thetamin
        self._thetamax = thetamax
        self._thetanaut = thetanaut
        self._dtheta=dtheta

        if self._single_dir:

            self._dtheta_s=dtheta_s

        return self

    def CreateRegularGrid(
            self,
            x0=0,y0=0,
            dx=100,dy=100,
            alpha=0,
            nz=1,
            deptfile='bed.dep',
            posdwn=True
            ):

        self._dx=dx
        self._dy=dy
        self._alpha=alpha
        self._nx = nx
        self._ny = ny
        self._nz = nz
        self._vardx=False
        self._xori=x0
        self._yori=y0

        self._depfile=os.path.join(path,depfile)
        z = self.OpenGridFile(self._xfile)
        zy,zx = z.shape
        self.nx=zx-1
        self.ny=zy-1
        self._posdwn=posdwn

        return self

    def LoadGridFromDirectory(
            self,
            path='.',
            xfile='x.grd',
            yfile='y.grd',
            depfile='bed.dep',
            posdwn=True
            ):

        if xfile:
            self._xfile=os.path.join(path,xfile)
            x = self.OpenGridFile(self._xfile)
            self._ny,self._nx=x.shape
        if yfile and xfifle:
            self._yfile=os.path.join(path,yfile)
            self._DelftGridFormat=False
        elif xfile and not yfile:
            self._yfile = None
            self._DelftGridFormat=True
        else:
            self._yfile = None

        self._depfile=os.path.join(path,depfile)
        z = self.OpenGridFile(self._xfile)
        zy,zx = z.shape
        if (self._nx+1 != zx) or (self._ny+1 != zy):
            raise ValueError('depth dimension must be nx+1 and ny+1')
        else:
            depfile=None

        self._vardx=True
        self._dx=False
        self._dy=False
        self._alpha=False
        self._posdwn=posdwn

        return self

    def OpenGridFile(fname):

        x = np.genfromtxt(fname)

        return x


    def WriteOutput(self,path):

        with open(os.path.join(path,'params.txt'),'w') as f:
            f.write(''.join(['\%' for i in range(75)]))
            f.write('\n')
            f.write('\%\%\%\ XBeach parameter settings input file                                \%\%\%\n')
            f.write('\%\%\%                                                                     \%\%\%\n')
            f.write('\%\%\%\ file created in : {}                                        \%\%\%\n'.format(datetime.today().strftime('%Y-%m-%d')))
            f.write('\%\%\%\ Input created with pyXbeach                                         \%\%\%\n')
            f.write(''.join(['\%' for i in range(75)]))
            f.write('\n')

            f.write('\n')
            f.write('\%\%\%\ Physical parameters \%\%\%\%\%\%\%\%\%\%\%\%\%\%\%\%\%\%\%\%\%\%\%\%\%\%\%\%\%\%\%\%\%\%\%\%\%\%\%\%\%\%\%\%\%\%\%\%\%\%\%')
            f.write('\n')
            f.write('\n')
            f.write('advection=%i' % int(self._advection))
            f.write('avalanching=%i' % int(self._avalanching))
            f.write('bchwiz=%i' % int(self._bchwiz))
            f.write('cyclic=%i' % int(self._cyclic))
            f.write('flow=%i' % int(self._flow))
            f.write('gwflow=%i' % int(self._gwflow))
            f.write('lwave=%i' % int(self._lwave))
            f.write('morphology=%i' % int(self._morphology))
            f.write('nonh=%i' % int(self._nonh))
            f.write('q3d=%i' % int(self._q3d))
            f.write('sedtrans=%i' % int(self._sedtrans))
            f.write('setbathy=%i' % int(self._setbathy))
            f.write('ships=%i' % int(self._ships))
            f.write('single_dir=%i' % int(self._single_dir))
            f.write('snells=%i' % int(self._snells))
            f.write('swave=%i' % int(self._swave))
            f.write('swrunupn=%i' % int(self._swrunup))
            f.write('vegetation=%i' % int(self._vegetation))
            f.write('viscosity=%i' % int(self._viscosity))
            f.write('wind=%i' % int(self._wind))

            if self._wavemodel=='surfbeat' of self._wavemodel=='stat' or self._wavemodel=='nonh'
                f.write('advection=%s' % int(self._wavemodel='surfbeat')
            else:
                raise ValueError('wavemodel must be stat,surfbeat or nonh')

            f.write('\n')
            f.write('\%\%\%\ Grid parameters \%\%\%\%\%\%\%\%\%\%\%\%\%\%\%\%\%\%\%\%\%\%\%\%\%\%\%\%\%\%\%\%\%\%\%\%\%\%\%\%\%\%\%\%\%\%\%\%\%\%\%\%\%\%\%')
            f.write('\n')
            f.write('\n')

            if self._dtheta > 180 or self._dtheta <0.1:
                raise ValueError('dtheta value must be between 0.1 and 180 degrees')
            else:
                f.write('dtheta= %1.3f\n' % self._dtheta)

            if self._dtheta_s > 20 or self._dtheta_s <0.1:
                raise ValueError('dtheta_2 value must be between 0.1 and 20 degrees')
            else:
                f.write('dtheta_s= %1.1f\n' % self._dtheta_s)

            f.write('thetanaut=%i\n' % int(self._thetanaut))

            f.write('vardx=%i\n' % int(self._vardx))

            if  not self_dx:
                if self._DelftGridFormat:
                    f.write('gridform=delft3d\n')
                    f.write('xyfile=%s\n' % self._xfile)
                else:
                    f.write('gridform=xbeach\n')
                    f.write('xfile=%s\n' % self._xfile)
                    f.write('yfile=%s\n' % self._yfile)
            else:
                if self._alpha > 360 or self._alpha <0:
                    raise ValueError('alpha value must be between 0 and 360 degrees')
                else:
                    f.write('alpha= %i\n' % self._alpha)
                if self._dx > 1000000000 or self._dx < 0:
                    raise ValueError('dx value must be between 0 and 1^9 m')
                else:
                    f.write('dx=%1.3f\n' % self._dx)
                if self._dy > 1000000000 or self._dy < 0:
                    raise ValueError('dy value must be between 0 and 1^9 m')
                else:
                    f.write('dy=%1.3f\n' % self._dy)
                if self._xori <-1000000000.0 or self._xori> 1000000000.0:
                    raise ValueError('xori value must be between -10^9 and 10^9')
                else:
                    f.write('xori=%1.2f\n' % self._xori)
                if self._yori <-1000000000.0 or self._yori> 1000000000.0:
                    raise ValueError('yori value must be between -10^9 and 10^9')
                else:
                    f.write('yori=%1.2f\n' % self._yori)

            if self._nx<2 or self._nx>10000:
                raise ValueError('nx value must be between 2 and 10000')
            else:
                f.write('nx= %i\n' % self._nx)

            if self._ny<0 or sel._ny>10000:
                raise ValueError('ny value must be between 0 and 10000')
            else:
                f.write('ny= %i\n' % self._ny)

            if self._nz<1 or sel._nz>100:
                raise ValueError('nz value must be between 1 and 100')
            else:
                f.write('ny= %i\n' % self._nz)

            f.write('deptfile=%s\n' % int(self._depfile))








        pass



                            ARC+
                            BRfac+
                            CFL
                            Cd+
                            Hrms
                            Tbfac+
                            Tlong
                            Tm01switch+
                            Topt+
                            Trep
                            Tsmin+
                            advection
                            alfa
                            alpha+
                            aquiferbot+
                            aquiferbotfile+
                            avalanching
                            back
                            bcfile
                            bchwiz
                            bclwonly
                            bdslpeffdir
                            bdslpeffdirfac
                            bdslpeffini
                            bdslpeffmag
                            bed+
                            bedfriccoef
                            bedfricfile
                            bedfriction
                            bermslope
                            beta+
                            betad+
                            break
                            breakerdelay+
                            breakviscfac+
                            breakvisclen+
                            bulk+
                            cats+
                            ci+
                            cm
                            cmax+
                            compi
                            correctHm0
                            cyclic
                            defuse
                            delta+
                            deltar
                            depfile*
                            depthscale+
                            dilatancy
                            dir0
                            disch_loc_file+
                            disch_timeseries_file+
                            dispc+
                            drifterfile
                            dryslp
                            dt
                            dtbc+
                            dtheta*
                            dthetaS_XB+
                            dtheta_s*
                            dtset
                            dwetlayer+
                            dx*
                            dy*
                            dzg1+
                            dzg2+
                            dzg3+
                            dzmax+
                            eps
                            eps_sd
                            epsi+
                            facAs+
                            facDc+
                            facSk+
                            facrun
                            facsd
                            facsl+
                            facua+
                            fallvelred
                            fcutoff+
                            flow
                            form
                            frac_dz+
                            freewave+
                            friction_acceleration
                            friction_infiltration
                            friction_turbulence
                            front
                            fwcutoff
                            g
                            gamma
                            gamma2
                            gamma_turb
                            gammax+
                            gridform
                            gw0+
                            gw0file+
                            gwReturb+
                            gwfastsolve
                            gwflow+
                            gwheadmodel+
                            gwhorinfil+
                            gwnonh+
                            gwscheme+
                            hmin
                            hotstartflow+
                            hswitch+
                            hwci+
                            hwcimax+
                            instat
                            irhog8
                            jetfac
                            kdmin+
                            kmax
                            kx+
                            ky+
                            kz+
                            lat+
                            lateralwave
                            left
                            lsgrad
                            lwave
                            lws+
                            lwt+
                            m
                            maxbrsteep+
                            maxdtfac
                            maxerror+
                            maxiter+
                            merge+
                            mmpi+
                            morfac
                            morfacopt+
                            morphology
                            morstart
                            morstop
                            mpiboundary+
                            n+
                            nc
                            ncfilename+
                            nd+
                            nd_var+
                            ndischarge+
                            ndrifter
                            ne_layer
                            ngd
                            nglobalvar
                            nhbreaker+
                            nhlay+
                            nmax+
                            nmeanvar
                            nmpi+
                            nonh+
                            nonhq3d
                            nonhspectrum+
                            npoints
                            npointvar
                            nrugauge
                            nrugdepth+
                            nsetbathy+
                            nship+
                            nspectrumloc+
                            nspr
                            ntdischarge+
                            nuh
                            nuhfac+
                            nuhv
                            nveg
                            nx*
                            ny*
                            nz
                            oldhu
                            order+
                            outputformat+
                            outputprecision
                            paulrevere
                            phit+
                            por
                            pormax
                            posdwn
                            projection+
                            px
                            q3d
                            random+
                            reformsteep+
                            remdryoutput
                            reposeangle
                            rfb+
                            rheeA
                            rho
                            rhoa+
                            rhog8
                            rhos
                            right
                            roller+
                            rotate
                            rt
                            rwave
                            scheme+
                            secbrsteep+
                            secorder+
                            sedtrans
                            setbathy
                            setbathyfile*+
                            shipfile
                            ships+
                            shoaldelay
                            sigfac
                            single_dir+
                            smag+
                            smax+
                            snells+
                            solver+
                            solver_acc+
                            solver_maxit+
                            solver_urelax+
                            sourcesink+
                            split+
                            sprdthr+
                            struct
                            sus+
                            swave
                            swkhmin
                            swrunup
                            sws+
                            t
                            taper
                            thetamax*
                            thetamin*
                            thetanaut
                            thetanum+
                            tideloc
                            tidetype+
                            timings+
                            tintc+
                            tintg
                            tintm
                            tintp
                            tnext
                            trepfac+
                            tsfac+
                            tsglobal+
                            tsmean+
                            tspoints+
                            tstart
                            tstop*
                            tunits+
                            turb+
                            turbadv+
                            umin
                            vardx
                            vegcanflo
                            vegetation+
                            veggiefile
                            veggiemapfile
                            vegnonlin
                            veguntow
                            vicmol
                            viscosity
                            vonkar
                            waveform
                            wavemodel
                            wavfriccoef
                            wavfricfile
                            wavint
                            wbctype
                            wbcversion
                            wci
                            wearth+
                            wetslp
                            wind
                            windfile
                            windth
                            windv
                            ws
                            xfile
                            xori
                            xyfile*
                            yfile
                            yori
                            z0+
                            zs0
                            zs0file
                            zsinitfile
        if xgrid:
