# Using Mike for Version Management

## Basic Commands

### Deploy a New Version
```bash
mike deploy 1.0
```

### Deploy with Alias
```bash
mike deploy 1.0 latest
```

### List Versions
```bash
mike list
```

### Set Default Version
```bash
mike set-default latest
```

## Version Management Workflow

1. Make documentation changes
2. Commit changes to git
3. Deploy new version
4. Update aliases if needed
5. Serve locally to verify

## Best Practices

1. Use semantic versioning
2. Maintain clear version notes
3. Test locally before deployment
4. Keep version aliases consistent