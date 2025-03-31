# Public API Reference

## Types of resources

### Package

```json
{
    "id": "...",
    "name": "...",
    "description": "...",
    "author_name": "...",
    "version": "...",
    "data": "...",
    "created_at": "...",
    "updated_at": "...",
}
```
### PackageInfo

```json
{
    "id": "...",
    "name": "...",
    "description": "...",
    "author_name": "...",
    "version": "...",
    "created_at": "...",
    "updated_at": "...",
}
```

> [!NOTE]
> `PackageInfo` does not contain `data` property

## Urls

All urls are relative `<domain>://public/api`

### Get Package

|Method|Url|Description|
|------|---|-----------|
|GET|`/packages/package`|Returns a package|

Request:
```json
{
    "package_id": "<id>"
}
```

Response:
```json
{
    "id": "...",
    "name": "...",
    "description": "...",
    "author_name": "...",
    "version": "...",
    "data": "...",
    "created_at": "...",
    "updated_at": "...",
}
```

### Get Package Info

|Method|Url|Description|
|------|---|-----------|
|GET|`/packages/package_info`|Returns a package|

Request:
```json
{
    "package_id": "<id>"
}
```

Response:
```json
{
    "id": "...",
    "name": "...",
    "description": "...",
    "author_name": "...",
    "version": "...",
    "created_at": "...",
    "updated_at": "...",
}
```

### Get Packages Information

|Method|Url|Description|
|------|---|-----------|
|GET|`/packages/packages_info`|Returns a package|

Request:
```json
{
    "package_name": "<name>"
}
```

Response:
```json
{
    "packages": [
        {
            "id": "...",
            "name": "...",
            "description": "...",
            "author_name": "...",
            "version": "...",
            "created_at": "...",
            "updated_at": "...",
        }
    ]
}
```
