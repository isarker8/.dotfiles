static const char normfgcolor[] = "#c7c8c8";
static const char normbgcolor[] = "#212324";
static const char normbordercolor[] = "#637a7a";

static const char selfgcolor[] = "#c7c8c8";
static const char selbgcolor[] = "#847A73";
static const char selbordercolor[] = "#c7c8c8";

static const char *colors[][3]      = {
    /*                  fg               bg             border             */
    [SchemeNorm]    = { normfgcolor,     normbgcolor,   normbordercolor }, // unfocused wins
    [SchemeSel]     = { selfgcolor,      selbgcolor,    selbordercolor },  // the focused win
	/* for bar --> {text, background, null} */
	[SchemeStatus]  = { normfgcolor,     normbgcolor,   normbgcolor  },    /* status R */
};
