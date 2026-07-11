%global tl_name seatingchart
%global tl_revision 76924

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.5.0
Release:	%{tl_revision}.1
Summary:	Generation of seating charts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/luatex/latex/seatingchart
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/seatingchart.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/seatingchart.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package enables the visualization of seating charts, whereby the
seating layouts (i.e. the arrangement of seats in a room) and the
seating scheme (i.e. the selection and labeling of occupied seats) can
be controlled independently of each other. The package should be
considered experimental and requires LuaLaTeX.

